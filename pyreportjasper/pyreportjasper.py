# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# 2024 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
import warnings
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
        'html',
        'pdf',
        'rtf',
        'docx',
        'odt',
        'xml',
        'xls',
        'xlsx',
        'csv',
        'csv_meta',
        'ods',
        'pptx',
        'jrprint',
        'stream_pdf'
    )

    METHODS = ('GET', 'POST', 'PUT')
    
    TypeJava = Report.TypeJava

    def config(self, input_file, output_file=False, output_formats=['pdf'], parameters={}, db_connection={},
               locale='en_US', resource=None, subreports=None, jvm_opts=()):
        if not input_file:
            raise NameError('No input file!')
        if isinstance(output_formats, list):
            if any([key not in self.FORMATS for key in output_formats]):
                raise NameError('Invalid format!')
        else:
            raise NameError("'output_formats' value is not list!")
        self.config = Config()
        self.config.input = input_file
        self.config.subreports = subreports if subreports else {}
        self.config.locale = locale
        self.config.resource = resource
        self.config.outputFormats = output_formats
        if output_file:
            self.config.output = output_file
        else:
            self.config.output = input_file
        self.config.params = parameters
        if len(db_connection) > 0:
            mapping = {
                'driver': 'dbType',
                'username': 'dbUser',
                'password': 'dbPasswd',
                'host': 'dbHost',
                'database': 'dbName',
                'port': 'dbPort',
                'jdbc_driver': 'dbDriver',
                'jdbc_url': 'dbUrl',
                'jdbc_dir': 'jdbcDir',
                'db_sid': 'dbSid',
                'db_multitenant': 'dbOracleMultitenant',
                'xml_xpath': 'xmlXpath',
                'data_file': 'dataFile',
                'data_url': 'data_url',
                'json_query': 'jsonQuery',
                'jsonql_query': 'jsonQLQuery',
                'csv_columns': 'csvColumns',
                'csv_record_del': 'csvRecordDel',
                'csv_field_del': 'csvFieldDel',
                'csv_out_field_del': 'outFieldDel',
                'csv_charset': 'csvCharset',
                'csv_out_charset': 'outCharset'
            }

            for key, value in db_connection.items():
                if key in mapping:
                    setattr(self.config, mapping[key], value)
                elif key == 'csv_first_row':
                    self.config.csvFirstRow = True

            self.config.jvm_opts = jvm_opts

    def compile(self, write_jasper=False):
        error = None
        if os.path.isfile(self.config.input):
            try:
                self.config.writeJasper = write_jasper
                report = Report(self.config, self.config.input)
                report.compile()
            except Exception as ex:
                error = NameError('Error compile file: {}'.format(str(ex)))
        elif os.path.isdir(self.config.input):
            list_files_dir = [arq for arq in os.listdir(str(self.config.input)) if os.path.isfile(arq)]
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
        else:
            return True
        
    def compile_all_jrxml_dir(self, dir):
        if os.path.isdir(dir):
            list_files_dir = [arq for arq in os.listdir(str(dir)) if os.path.isfile(arq)]
            list_jrxml = [arq for arq in list_files_dir if arq.lower().endswith(".jrxml")]
            for file in list_jrxml:
                try:
                    file_imput = os.path.join(dir, file)
                    with open(file_imput, 'rb') as file_bytes:
                        self.config.writeJasper = True
                        print("Compiling: {}".format(file_imput))
                        report = Report(self.config, file_imput)
                        report.input_file = file_imput
                        report.jasper_design = report.JRXmlLoader.load(report.ByteArrayInputStream(file_bytes.read()))
                        report.initial_input_type = 'JASPER_DESIGN'
                        report.compile_to_file()
                except Exception as ex:
                    error = NameError('Error compile file: {}'.format(str(ex)))
                    print(error)
        else:
            print("Value entered as a parameter is not a directory")

    def instantiate_report(self):
        report = Report(self.config, self.config.input)
        report.fill()
        return report        

    def process_report(self):
        error = None
        base_input = os.path.splitext(self.config.input)
        if base_input[-1] == ".jrxml":
            new_input = base_input[0] + ".jasper"
            if os.path.isfile(new_input):
                self.config.input = new_input

        if os.path.isfile(self.config.input):
            try:
                report = self.instantiate_report()
                try:
                    formats_functions = {
                        'pdf': report.export_pdf,
                        'html': report.export_html,
                        'rtf': report.export_rtf,
                        'docx': report.export_docx,
                        'odt': report.export_odt,
                        'xml': report.export_xml,
                        'xls': report.export_xls,
                        'xlsx': report.export_xlsx,
                        'csv': report.export_csv,
                        'csv_meta': report.export_csv_meta,
                        'ods': report.export_ods,
                        'pptx': report.export_pptx,
                        'jrprint': report.export_jrprint,
                        'stream_pdf': report.fetch_pdf_report
                    }

                    for f in self.config.outputFormats:
                        export_function = formats_functions.get(f)
                        if export_function:
                            if f == 'stream_pdf':
                               pdf_bytes =export_function()
                            else:
                                export_function()
                        else:
                            raise NameError("Error output format {} not implemented!".format(f))
                    return pdf_bytes
                except Exception as ex:
                    error = NameError("Error export format: {}".format(ex))
            except Exception as ex:
                error = NameError('Error fill report: {}'.format(str(ex)))
        else:
            error = NameError('Error: not a file: {}'.format(self.config.input))
        if error:
            raise error
        return True

    def list_report_params(self):
        report = Report(self.config, self.config.input)
        report.fill()
        result = report.get_report_parameters()
        list_param = []
        i = 0
        while i < result.length:
            list_param.append(str(result[i].getName()))
            i += 1
        return list_param

    def process(self, input_file, output_file=False, format_list=['pdf'],
                parameters={}, db_connection={}, locale='en_US', resource=""):
        warnings.warn("process is deprecated - use config and then process_report instead. See the documentation "
                      "https://pyreportjasper.readthedocs.io",
                      DeprecationWarning)
        self.config(
            input_file=input_file,
            output_file=output_file,
            output_formats=format_list,
            parameters=parameters,
            db_connection=db_connection,
            locale=locale,
            resource=resource
        )
        self.process_report()
