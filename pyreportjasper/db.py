# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# 2023 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
import jpype
import pathlib
import jpype.imports

from pyreportjasper.config import Config


class Db:
    Connection = None
    DriverManager = None
    Class = None
    JRXmlDataSource = None
    JsonDataSource = None
    JsonQLDataSource = None
    HikariDataSource = None

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
        self.URL = jpype.JPackage('java').net.URL
        self.ByteArrayInputStream = jpype.JPackage('java').io.ByteArrayInputStream
        self.HikariDataSource = jpype.JPackage('com.zaxxer.hikari').HikariDataSource
        self.HikariConfig = jpype.JPackage('com.zaxxer.hikari').HikariConfig
        self.config_pool = None

    def initialize_pool(self, config: Config):
        dbtype = config.dbType
        host = config.dbHost
        user = config.dbUser
        passwd = config.dbPasswd
        driver = None
        dbname = None
        port = None
        sid = None
        connect_string = None
        multitenant = None

        if dbtype == "mysql":
            driver = config.dbDriver
            port = config.dbPort or 3306
            dbname = config.dbName
            connect_string = f"jdbc:mysql://{host}:{port}/{dbname}?useSSL=false"
        elif dbtype == "postgres":
            driver = config.dbDriver
            port = config.dbPort or 5434
            dbname = config.dbName
            connect_string = f"jdbc:postgresql://{host}:{port}/{dbname}"
        elif dbtype == "oracle":
            driver = config.dbDriver
            port = config.dbPort or 1521
            sid = config.dbSid
            multitenant = config.dbOracleMultitenant
            connect_string = (
                f"jdbc:oracle:thin:@{host}:{port}/{sid}" if multitenant else f"jdbc:oracle:thin:@{host}:{port}:{sid}"
            )
        elif dbtype == "generic":
            driver = config.dbDriver
            connect_string = config.dbUrl

        self.Class.forName(driver)
        hikari_config = self.HikariConfig()
        hikari_config.setJdbcUrl(connect_string)
        hikari_config.setUsername(user)
        hikari_config.setPassword(passwd)
        hikari_config.setMaximumPoolSize(10)  # Máximo de conexiones en el pool
        hikari_config.setMinimumIdle(2)  # Mínimo de conexiones en el pool
        hikari_config.setIdleTimeout(30000)  # Tiempo de espera para conexiones inactivas (ms)
        hikari_config.setConnectionTimeout(10000)  # Tiempo de espera para obtener una conexión (ms)

        self.config_pool = self.HikariDataSource(hikari_config)

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
        if config.dataURL:
            ds = self.JsonDataSource(self.get_data_url_input_stream(config), config.jsonQuery)
        else:
            ds = self.JsonDataSource(self.get_data_file_input_stream(config), config.jsonQuery)
        return jpype.JObject(ds, self.JsonDataSource)

    def get_jsonql_datasource(self, config: Config):
        ds = self.JsonQLDataSource(self.get_data_file_input_stream(config), config.jsonQLQuery)
        return jpype.JObject(ds, self.JsonQLDataSource)

    def get_data_file_input_stream(self, config: Config):
        data_file = config.dataFile
        bytes_data_file = None
        if isinstance(data_file, str) or isinstance(data_file, pathlib.PurePath):
            if not os.path.isfile(data_file):
                raise NameError("dataFile is not file")
            with open(data_file, "rb") as file:
                bytes_data_file = file.read()
        elif isinstance(data_file, bytes):
            bytes_data_file = data_file
        else:
            raise NameError("dataFile does not have a valid type. Please enter the file path or its bytes")
        return self.ByteArrayInputStream(bytes_data_file)

    def get_data_url_input_stream(self, config: Config):
        return self.JRLoader.getInputStream(self.URL(config.dataURL))

    def get_connection(self):
        if self.config_pool is None:
            raise NameError("El pool de conexiones no está inicializado.")
        return self.config_pool.getConnection()
