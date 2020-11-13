# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#
import jpype


class Config:
    askFilter = None
    command = None
    dbDriver = None
    dbHost = None
    dbName = None
    dbPasswd = None
    dbPort = None
    dbSid = None
    dbType = None
    dbUrl = None
    dbUser = None
    verbose = None
    input = None
    jdbcDir = None
    dataFile = None
    csvFirstRow = None
    csvColumns = None
    csvRecordDel = None
    csvFieldDel = None
    csvCharset = None
    xmlXpath = None
    jsonQuery = None
    jsonQLQuery = None
    locale = 'pt_BR'
    output = None
    outputFormats = None
    params = None
    printerName = None
    reportName = None
    resource = None
    withPrintDialog = None
    writeJasper = True
    copies = None
    outFieldDel = None
    outCharset = None

    jvm_maxmem = '512M'
    jvm_classpath = None

    def __init__(self):
        self.JRLoader = jpype.JPackage('net').sf.jasperreports.engine.util.JRLoader

    def has_output(self):
        return False if self.output is None else True

    def is_write_jasper(self):
        return bool(self.writeJasper)

    def get_data_file_input_stream(self):
        return self.JRLoader.getInputStream(self.dataFile)
