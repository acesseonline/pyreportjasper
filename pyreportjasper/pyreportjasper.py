# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
from pyreportjasper.config import Config
from pyreportjasper.report import Report


class PyReportJasper:
    config = None
    DSTYPES = (
        "none",
        "csv",
        "xml",
        "json",
        "jsonql",
        "mysql",
        "postgres",
        "oracle",
        "generic"
    )

    FORMATS = (
        'pdf',
        'rtf',
        'docx',
        'odt',
        'xml',
        'xls',
        'xlsx',
        'csv',
        'ods',
        'pptx',
    )

    METHODS = ('GET', 'POST', 'PUT')

    def set_up(self, input_file, output_file=False, output_formats=['pdf'], parameters={}, db_connection={},
               locale='pt_BR', resource=None):
        if not input_file:
            raise NameError('No input file!')
        if isinstance(output_formats, list):
            if any([key not in self.FORMATS for key in output_formats]):
                raise NameError('Invalid format!')
        else:
            raise NameError("'output_formats' value is not list!")
        self.config = Config()
        self.config.input = input_file
        self.config.locale = locale
        self.config.resource = resource
        self.config.outputFormats = output_formats
        if output_file:
            self.config.output = output_file
        else:
            self.config.output = input_file
        self.config.params = parameters
        if len(db_connection) > 0:
            self.config.dbType = db_connection['driver']
            if 'username' in db_connection:
                self.config.dbUser = db_connection['username']
            if 'password' in db_connection:
                self.config.dbPasswd = db_connection['password']
            if 'host' in db_connection:
                self.config.dbHost = db_connection['host']
            if 'database' in db_connection:
                self.config.dbName = db_connection['database']
            if 'port' in db_connection:
                self.config.dbPort = db_connection['port']
            if 'jdbc_driver' in db_connection:
                self.config.dbDriver = db_connection['jdbc_driver']
            if 'jdbc_url' in db_connection:
                self.config.dbUrl = db_connection['jdbc_url']
            if 'jdbc_dir' in db_connection:
                self.config.jdbcDir = db_connection['jdbc_dir']
            if 'db_sid' in db_connection:
                self.config.dbSid = db_connection['db_sid']
            if 'xml_xpath' in db_connection:
                self.config.xmlXpath = db_connection['xml_xpath']
            if 'data_file' in db_connection:
                self.config.dataFile = db_connection['data_file']
            if 'json_query' in db_connection:
                self.config.jsonQuery = db_connection['json_query']
            if 'jsonql_query' in db_connection:
                self.config.jsonQLQuery = db_connection['jsonql_query']
            if 'csv_first_row' in db_connection:
                self.config.csvFirstRow = True
            if 'csv_columns' in db_connection:
                self.config.csvColumns = db_connection['csv_columns']
            if 'csv_record_del' in db_connection:
                self.config.csvRecordDel = db_connection['csv_record_del']
            if 'csv_field_del' in db_connection:
                self.config.csvFieldDel = db_connection['csv_field_del']
            if 'csv_charset' in db_connection:
                self.config.csvCharset = db_connection['csv_charset']

    def compile(self):
        error = None
        if os.path.isfile(self.config.input):
            try:
                report = Report(self.config, self.config.input)
                report.compile()
            except Exception as ex:
                error = NameError('Error compile file: {}'.format(str(ex)))
        elif os.path.isdir(self.config.input):
            list_files_dir = [arq for arq in self.config.input if os.path.isfile(arq)]
            list_jrxml = [arq for arq in list_files_dir if arq.lower().endswith(".jrxml")]
            for file in list_jrxml:
                try:
                    print("Compiling: {}".format(str(file)))
                    report = Report(self.config, file)
                    report.compile()
                except Exception as ex:
                    error = NameError('Error compile file: {}'.format(str(ex)))
        else:
            error = NameError('Error: not a file: {}'.format(self.config.input))

        if error:
            raise error

    def process_report(self):
        error = None
        base_input = os.path.splitext(self.config.input)
        if base_input[-1] == ".jrxml":
            new_input = base_input[0] + ".jasper"
            if os.path.isfile(new_input):
                self.config.input = new_input

        if os.path.isfile(self.config.input):
            try:
                report = Report(self.config, self.config.input)
                report.fill()
                try:
                    formats = self.config.outputFormats
                    for f in formats:
                        if f == 'pdf':
                            report.export_pdf()
                        elif f == 'rtf':
                            report.export_rtf()
                        elif f == 'docx':
                            report.export_docx()
                        elif f == 'odt':
                            report.export_odt()
                        elif f == 'xml':
                            report.export_xml()
                        elif f == 'xls':
                            report.export_xls()
                        elif f == 'xlsx':
                            report.export_xlsx()
                        elif f == 'csv':
                            report.export_csv()
                        elif f == 'ods':
                            report.export_ods()
                        elif f == 'pptx':
                            report.export_pptx()
                        else:
                            raise NameError("Error output format {} not implemented!".format(f))
                except Exception as ex:
                    error = NameError("Error export format: {}".format(ex))
            except Exception as ex:
                error = NameError('Error fill report: {}'.format(str(ex)))
        else:
            error = NameError('Error: not a file: {}'.format(self.config.input))
        if error:
            raise error


    def list_report_params(self):
        # TODO: To implement
        pass
