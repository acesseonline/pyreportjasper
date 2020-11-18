# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

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
    params = {}
    printerName = None
    reportName = None
    resource = None
    withPrintDialog = None
    writeJasper = False
    copies = None
    outFieldDel = None
    outCharset = None

    jvm_maxmem = '512M'
    jvm_classpath = None

    def has_output(self):
        return False if self.output is None else True

    def is_write_jasper(self):
        return bool(self.writeJasper)

    def has_jdbc_dir(self):
        return True if self.jdbcDir else False

    def has_resource(self):
        return True if self.resource else False
