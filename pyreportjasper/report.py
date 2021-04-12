# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#
import os
import jpype
import time
from pyreportjasper.config import Config
from pyreportjasper.db import Db


class Report:
    config = None
    input_file = None
    defaultLocale = None
    initial_input_type = None
    output = None

    def __init__(self, config: Config, input_file):
        self.SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
        self.LIB_PATH = os.path.join(self.SCRIPT_DIR, 'libs')
        self.JDBC_PATH = os.path.join(self.LIB_PATH, 'jdbc')
        if not os.path.exists(self.LIB_PATH):
            raise NameError('Library directory not found at {0}'.format(self.LIB_PATH))
        self.config = config
        if not jpype.isJVMStarted():
            classpath = [
                os.path.join(self.LIB_PATH, "*"),
                os.path.join(self.JDBC_PATH, "*"),
            ]

            if self.config.resource:
                classpath.append(os.path.join(self.config.resource, "*"))

            if self.config.jvm_classpath:
                classpath.append(self.config.jvm_classpath)

            if self.config.jvm_classpath is None:
                jpype.startJVM("-Djava.system.class.loader=org.update4j.DynamicClassLoader",
                               "-Xmx{}".format(self.config.jvm_maxmem),
                               classpath=classpath)

        self.Locale = jpype.JPackage('java').util.Locale
        self.jvJRLoader = jpype.JPackage('net').sf.jasperreports.engine.util.JRLoader
        self.JasperReport = jpype.JPackage('net').sf.jasperreports.engine.JasperReport
        self.JasperPrint = jpype.JPackage('net').sf.jasperreports.engine.JasperPrint
        self.JRXmlLoader = jpype.JPackage('net').sf.jasperreports.engine.xml.JRXmlLoader
        self.jvJasperCompileManager = jpype.JPackage('net').sf.jasperreports.engine.JasperCompileManager
        self.LocaleUtils = jpype.JPackage('org').apache.commons.lang.LocaleUtils
        self.Locale = jpype.JPackage('java').util.Locale
        self.jvJasperFillManager = jpype.JPackage('net').sf.jasperreports.engine.JasperFillManager
        self.JREmptyDataSource = jpype.JPackage('net').sf.jasperreports.engine.JREmptyDataSource
        self.JasperExportManager = jpype.JPackage('net').sf.jasperreports.engine.JasperExportManager
        self.FileOutputStream = jpype.JPackage('java').io.FileOutputStream
        self.JRRtfExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRRtfExporter
        self.SimpleExporterInput = jpype.JPackage('net').sf.jasperreports.export.SimpleExporterInput
        self.SimpleWriterExporterOutput = jpype.JPackage('net').sf.jasperreports.export.SimpleWriterExporterOutput
        self.JRDocxExporter = jpype.JPackage('net').sf.jasperreports.engine.export.ooxml.JRDocxExporter
        self.JRPptxExporter = jpype.JPackage('net').sf.jasperreports.engine.export.ooxml.JRPptxExporter
        self.JRXlsxExporter = jpype.JPackage('net').sf.jasperreports.engine.export.ooxml.JRXlsxExporter
        self.SimpleOutputStreamExporterOutput = jpype.JPackage('net').sf.jasperreports.export.SimpleOutputStreamExporterOutput
        self.JROdsExporter = jpype.JPackage('net').sf.jasperreports.engine.export.oasis.JROdsExporter
        self.JROdtExporter = jpype.JPackage('net').sf.jasperreports.engine.export.oasis.JROdtExporter
        self.SimpleHtmlExporterOutput = jpype.JPackage('net').sf.jasperreports.export.SimpleHtmlExporterOutput
        self.JRXmlExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRXmlExporter
        self.SimpleXmlExporterOutput = jpype.JPackage('net').sf.jasperreports.export.SimpleXmlExporterOutput
        self.HashMap = jpype.JPackage('java').util.HashMap
        self.JRXlsExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRXlsExporter
        self.SimpleXlsReportConfiguration = jpype.JPackage('net').sf.jasperreports.export.SimpleXlsReportConfiguration
        self.JRXlsMetadataExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRXlsMetadataExporter
        self.SimpleXlsMetadataReportConfiguration = jpype.JPackage('net').sf.jasperreports.export.SimpleXlsMetadataReportConfiguration
        self.JRXlsxExporter = jpype.JPackage('net').sf.jasperreports.engine.export.ooxml.JRXlsxExporter
        self.SimpleXlsxReportConfiguration = jpype.JPackage('net').sf.jasperreports.export.SimpleXlsxReportConfiguration
        self.JRCsvExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRCsvExporter
        self.SimpleCsvExporterConfiguration = jpype.JPackage('net').sf.jasperreports.export.SimpleCsvExporterConfiguration
        self.JRCsvMetadataExporter = jpype.JPackage('net').sf.jasperreports.engine.export.JRCsvMetadataExporter
        self.SimpleCsvMetadataExporterConfiguration = jpype.JPackage('net').sf.jasperreports.export.SimpleCsvMetadataExporterConfiguration
        self.JRSaver = jpype.JPackage('net').sf.jasperreports.engine.util.JRSaver
        self.File = jpype.JPackage('java').io.File
        self.ApplicationClasspath = jpype.JPackage('br').com.acesseonline.classpath.ApplicationClasspath
        self.input_file = input_file
        self.defaultLocale = self.Locale.getDefault()
        if self.config.has_resource():
            self.add_jar_class_path(self.config.resource)
        if self.config.has_resource():
            if os.path.isdir(self.config.resource):
                try:
                    res = self.File(self.config.resource)
                    self.ApplicationClasspath.add(res)
                except Exception as ex:
                    raise NameError(
                        'It was not possible to add the path {0} to the Class Path: ERROR: {1}'\
                        .format(self.config.resource, str(ex)))

        if self.config.has_jdbc_dir():
            self.add_jar_class_path(self.config.jdbcDir)

        try:
            # This fails in case of an jrxml file
            j_object = self.jvJRLoader.loadObject(self.File(input_file))
            cast_error = True
            try:
                self.jasper_report = jpype.JObject(j_object, self.JasperReport)
                cast_error = False
                self.initial_input_type = 'JASPER_REPORT'
            except:
                # nothing to do here
                pass
            try:
                self.jasper_print = jpype.JObject(j_object, self.JasperPrint)
                cast_error = False
                self.initial_input_type = 'JASPER_PRINT'
            except:
                # nothing to do here
                pass

            if cast_error:
                raise NameError('input file: {0} is not of a valid type'.format(self.input_file))
        except Exception:
            try:
                self.jasper_design = self.JRXmlLoader.load(input_file)
                self.initial_input_type = 'JASPER_DESIGN'
                self.compile()
            except Exception as ex:
                raise NameError('input file: {0} is not a valid jrxml file:'.format(str(ex)))

    def compile(self):
        self.jasper_report = self.jvJasperCompileManager.compileReport(self.input_file)
        if self.config.is_write_jasper():
            if self.config.output:
                base = os.path.splitext(self.config.output)[0]
            else:
                base = os.path.splitext(self.input_file)[0]
            new_input = base + ".jasper"
            self.JRSaver.saveObject(self.jasper_report, new_input)
            self.config.input = new_input

    def compile_to_file(self):
        """
        Emit a .jasper compiled version of the report definition .jrxml file.
        :return:
        """
        if self.initial_input_type == "JASPER_DESIGN":
            try:
                base = os.path.splitext(self.config.output)[0]
                self.JRSaver.saveObject(self.jasper_report, base + ".jasper")
            except Exception as ex:
                raise NameError('outputFile {}.jasper could not be written: {}'.format(base, ex))
        else:
            raise NameError('input file: {0} is not a valid jrxml file'.format(self.input_file))

    def fill(self):
        self.fill_internal()

    def fill_internal(self):
        parameters = self.HashMap()
        for key in self.config.params:
            parameters.put(key, self.config.params[key])
        try:
            if self.config.locale:
                self.config.locale = self.LocaleUtils.toLocale(self.config.locale)
                self.Locale.setDefault(self.config.locale)

            if self.config.dbType is None:
                empty_data_source = self.JREmptyDataSource()
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters,
                                                                        empty_data_source)
            elif self.config.dbType == 'csv':
                db = Db()
                ds = db.get_csv_datasource(self.config)
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters, ds)
            elif self.config.dbType == 'xml':
                if self.config.xmlXpath is None:
                    self.config.xmlXpath = self.get_main_dataset_query()
                db = Db()
                ds = db.get_xml_datasource(self.config)
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters, ds)
            elif self.config.dbType == 'json':
                if self.config.jsonQuery is None:
                    # try to get json query stored in the report
                    self.config.jsonQuery = self.get_main_dataset_query()
                db = Db()
                ds = db.get_json_datasource(self.config)
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters, ds)
            elif self.config.dbType == 'jsonql':
                if self.config.jsonQLQuery is None:
                    # try to get jsonql query stored in the report
                    self.config.jsonQuery = self.get_main_dataset_query()
                db = Db()
                ds = db.get_jsonql_datasource(self.config)
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters, ds)
            else:
                db = Db()
                con = db.get_connection(self.config)
                self.jasper_print = self.jvJasperFillManager.fillReport(self.jasper_report, parameters, con)
                con.close()
        except Exception as ex:
            raise NameError('Erro fill internal: {}'.format(str(ex)))

    def get_output_stream(self, suffix):
        """
         Return a file-based output stream with the given suffix
        :param suffix:
        :return: FileOutputStream
        """
        if os.path.isdir(self.config.output):
            base = os.path.basename(self.input_file)
            name_file = os.path.splitext(base)[0]
            output_path = os.path.splitext(self.config.output)[0] + name_file + suffix
        else:
            output_path = os.path.splitext(self.config.output)[0] + suffix
        try:
            output_stream = self.FileOutputStream(self.File(output_path))
            return output_stream
        except Exception as ex:
            raise NameError('Unable to create outputStream to {}: {}'.format(output_path, str(ex)))

    def export_pdf(self):
        self.JasperExportManager.exportReportToPdfStream(self.jasper_print, self.get_output_stream('.pdf'))

    def export_rtf(self):
        exporter = self.JRRtfExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleWriterExporterOutput(self.get_output_stream('.rtf')))

    def export_docx(self):
        exporter = self.JRDocxExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.docx')))
        exporter.exportReport()

    def export_odt(self):
        exporter = self.JROdtExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.odt')))
        exporter.exportReport()

    def export_xml(self):
        exporter = self.JRXmlExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        output_stream = self.SimpleXmlExporterOutput(self.get_output_stream(".xml"))
        output_stream.setEmbeddingImages(False)
        exporter.setExporterOutput(output_stream)
        exporter.exportReport()

    def export_xls(self):
        date_formats = self.HashMap()
        date_formats.put("EEE, MMM d, yyyy", "ddd, mmm d, yyyy")
        exporter = self.JRXlsExporter()
        rep_config = self.SimpleXlsReportConfiguration()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.xls')))
        rep_config.setDetectCellType(True)
        rep_config.setFormatPatternsMap(date_formats)
        exporter.setConfiguration(rep_config)
        exporter.exportReport()

    def export_xls_meta(self):
        date_formats = self.HashMap()
        date_formats.put("EEE, MMM d, yyyy", "ddd, mmm d, yyyy")
        exporter = self.JRXlsMetadataExporter()
        rep_config = self.SimpleXlsMetadataReportConfiguration()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.xls')))
        rep_config.setDetectCellType(True)
        rep_config.setFormatPatternsMap(date_formats)
        exporter.setConfiguration(rep_config)
        exporter.exportReport()

    def export_xlsx(self):
        date_formats = self.HashMap()
        date_formats.put("EEE, MMM d, yyyy", "ddd, mmm d, yyyy")
        exporter = self.JRXlsxExporter()
        rep_config = self.SimpleXlsxReportConfiguration()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.xlsx')))
        rep_config.setDetectCellType(True)
        rep_config.setFormatPatternsMap(date_formats)
        exporter.setConfiguration(rep_config)
        exporter.exportReport()

    def export_csv(self):
        exporter = self.JRCsvExporter()
        configuration = self.SimpleCsvExporterConfiguration()
        configuration.setFieldDelimiter(self.config.outFieldDel)
        exporter.setConfiguration(configuration)
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(
            self.SimpleWriterExporterOutput(self.get_output_stream(".csv"), self.config.outCharset))
        exporter.exportReport()

    def export_csv_meta(self):
        exporter = self.JRCsvMetadataExporter()
        configuration = self.SimpleCsvMetadataExporterConfiguration()
        configuration.setFieldDelimiter(self.config.outFieldDel)
        exporter.setConfiguration(configuration)
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(
            self.SimpleWriterExporterOutput(self.get_output_stream(".csv"), self.config.outCharset))
        exporter.exportReport()

    def export_ods(self):
        exporter = self.JROdsExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.ods')))
        exporter.exportReport()

    def export_pptx(self):
        exporter = self.JRPptxExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleOutputStreamExporterOutput(self.get_output_stream('.pptx')))
        exporter.exportReport()

    def export_jrprint(self):
        self.JRSaver.saveObject(self.jasper_print, self.get_output_stream('.jrprint'))

    def get_report_parameters(self):
        """
            getReportParameters
        :return: an List of {@link net.sf.jasperreports.engine.JRParameter} objects
        """
        if self.jasper_report is not None:
            return_val = self.jasper_report.getParameters()
            return return_val
        else:
            raise NameError("Parameters could not be read from {}".format(self.input_file))

    def get_main_dataset_query(self):
        """
             For JSON, JSONQL and any other data types that need a query to be provided,
             an obvious default is to use the one written into the report, since that is
             likely what the report designer debugged/intended to be used. This provides
             access to the value so it can be used as needed.
        :return: str of main dataset query
        """
        if self.initial_input_type == "JASPER_DESIGN":
            return self.jasper_design.getMainDesignDataset().getQuery().getText()
        elif self.initial_input_type == "JASPER_REPORT":
            return self.jasper_report.getMainDataset().getQuery().getText()
        else:
            raise NameError('No query for input type: {}'.format(self.initial_input_type))

    def add_jar_class_path(self, dir_or_jar):
        try:
            if os.path.isdir(dir_or_jar):
                jpype.addClassPath(os.path.join(dir_or_jar, "*"))
            elif os.path.splitext(dir_or_jar)[-1] == '.jar':
                jpype.addClassPath(dir_or_jar)
        except Exception as ex:
            raise NameError("Error adding class path: {}".format(ex))

