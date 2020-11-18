# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import jpype
import jpype.imports

from pyreportjasper.config import Config


class Db:
    Connection = None
    DriverManager = None
    Class = None
    JRXmlDataSource = None
    JsonDataSource = None
    JsonQLDataSource = None

    def __init__(self):
        self.Connection = jpype.JPackage('java').sql.Connection
        self.DriverManager = jpype.JPackage('java').sql.DriverManager
        self.Class = jpype.JPackage('java').lang.Class
        self.JRCsvDataSource = jpype.JPackage('net').sf.jasperreports.engine.data.JRCsvDataSource
        self.JRXmlDataSource = jpype.JPackage('net').sf.jasperreports.engine.data.JRXmlDataSource
        self.JsonDataSource = jpype.JPackage('net').sf.jasperreports.engine.data.JsonDataSource
        self.JsonQLDataSource = jpype.JPackage('net').sf.jasperreports.engine.data.JsonQLDataSource
        self.JRLoader = jpype.JPackage('net').sf.jasperreports.engine.util.JRLoader
        self.StringEscapeUtils = jpype.JPackage('org').apache.commons.lang.StringEscapeUtils
        self.File = jpype.JPackage('java').io.File

    def get_csv_datasource(self, config: Config):
        ds = self.JRCsvDataSource(self.get_data_file_input_stream(config), config.csvCharset)
        ds.setUseFirstRowAsHeader(jpype.JObject(jpype.JBoolean(config.csvFirstRow)))
        if config.csvFirstRow:
            ds.setColumnNames(config.csvColumns)
        ds.setRecordDelimiter(self.StringEscapeUtils.unescapeJava(config.csvRecordDel))
        ds.setFieldDelimiter(config.csvFieldDel)
        return jpype.JObject(ds, self.JRCsvDataSource)

    def get_xml_datasource(self, config: Config):
        ds = self.JRXmlDataSource(self.get_data_file_input_stream(config), config.xmlXpath)
        return jpype.JObject(ds, self.JRXmlDataSource)

    def get_json_datasource(self, config: Config):
        ds = self.JsonDataSource(self.get_data_file_input_stream(config), config.jsonQuery)
        return jpype.JObject(ds, self.JsonDataSource)

    def get_jsonql_datasource(self, config: Config):
        ds = self.JsonQLDataSource(self.get_data_file_input_stream(config), config.jsonQLQuery)
        return jpype.JObject(ds, self.JsonQLDataSource)

    def get_data_file_input_stream(self, config: Config):
        return self.JRLoader.getInputStream(self.File(config.dataFile))

    def get_connection(self, config: Config):
        dbtype = config.dbType
        host = config.dbHost
        user = config.dbUser
        passwd = config.dbPasswd
        driver = None
        dbname = None
        port = None
        sid = None
        connect_string = None

        if dbtype == "mysql":
            driver = config.dbDriver
            port = config.dbPort or 3306
            dbname = config.dbName
            connect_string = "jdbc:mysql://{}:{}/{}?useSSL=false".format(host, port, dbname)
        elif dbtype == "postgres":
            driver = config.dbDriver
            port = config.dbPort or 5434
            dbname = config.dbName
            connect_string = "jdbc:postgresql://{}:{}/{}".format(host, port, dbname)
        elif dbtype == "oracle":
            driver = config.dbDriver
            port = config.dbPort or 1521
            sid = config.dbSid
            connect_string = "jdbc:oracle:thin:@{}:{}:{}".format(host, port, sid)
        elif dbtype == "generic":
            driver = config.dbDriver
            connect_string = config.dbUrl

        self.Class.forName(driver)
        conn = self.DriverManager.getConnection(connect_string, user, passwd)
        return conn
