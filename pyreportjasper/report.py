# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# 2024 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#
import os
import jpype
import pathlib
from pyreportjasper.config import Config
from pyreportjasper.db import Db
import jpype.imports
from jpype.types import *
from enum import Enum


class Report:
    config = None
    input_file = None
    defaultLocale = None
    initial_input_type = None
    output = None
    
    TypeJava = Enum('TypeJava', [
                             ('BigInteger', 'java.math.BigInteger'),
                             ('Array', 'java.lang.reflect.Array'),
                             ('ArrayList', 'java.util.ArrayList'),
                             ('String', 'java.lang.String'),
                             ('Integer', 'java.lang.Integer'),
                             ('Boolean', 'java.lang.Boolean'),
                             ('Float', 'java.lang.Float'), 
                             ('Date', 'java.util.Date'),
                             #TODO: Not yet implemented
                            #  ('List', 'java.util.List'),
                            #  ('Currency', 'java.util.Currency'),
                            #  ('Image', 'java.awt.Image'),                             
                            #  ('Byte', 'java.lang.Byte'),
                            #  ('Character', 'java.lang.Character'), 
                            #  ('Short', 'java.lang.Short'),                             
                            #  ('Long', 'java.lang.Long'),
                            #  ('Float', 'java.lang.Float'), 
                            #  ('Double', 'java.lang.Double'),                             
                        ])
  

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

            if self.config.resource and os.path.isdir(self.config.resource):
                classpath.append(os.path.join(self.config.resource, "*"))

            if self.config.jvm_classpath:
                classpath.append(self.config.jvm_classpath)

            if self.config.jvm_classpath is None:
                jvm_args = [
                    "-Djava.system.class.loader=org.update4j.DynamicClassLoader",
                    "-Dlog4j.configurationFile={}".format(
                        os.path.join(self.LIB_PATH, 'log4j2.xml')),
                    "-XX:InitialHeapSize=512M",
                    "-XX:CompressedClassSpaceSize=64M",
                    "-XX:MaxMetaspaceSize=128M",                            
                    "-Xmx{}".format(self.config.jvm_maxmem),
                ]
                jvm_args.extend(self.config.jvm_opts or ())
                jpype.startJVM(*jvm_args, classpath=classpath)

        self.Locale = jpype.JPackage('java').util.Locale
        self.String = jpype.JPackage('java').lang.String
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
        self.HtmlExporter = jpype.JPackage('net').sf.jasperreports.engine.export.HtmlExporter
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
        self.ByteArrayInputStream = jpype.JPackage('java').io.ByteArrayInputStream
        self.ByteArrayOutputStream = jpype.JPackage('java').io.ByteArrayOutputStream
        self.ApplicationClasspath = jpype.JPackage('br').com.acesseonline.classpath.ApplicationClasspath

        if self.config.useJaxen:
            self.DefaultJasperReportsContext = jpype.JPackage('net').sf.jasperreports.engine.DefaultJasperReportsContext
            self.context = self.DefaultJasperReportsContext.getInstance();
            self.JRPropertiesUtil = jpype.JPackage('net').sf.jasperreports.engine.JRPropertiesUtil
            self.JRPropertiesUtil.getInstance(self.context).setProperty("net.sf.jasperreports.xpath.executer.factory",
                "net.sf.jasperreports.engine.util.xml.JaxenXPathExecuterFactory");

        if isinstance(input_file, str) or isinstance(input_file, pathlib.PurePath):
            if not os.path.isfile(input_file):
                raise NameError('input_file is not file.')
            with open(input_file, 'rb') as file:
                self.input_file = file.read()        
        elif isinstance(input_file, bytes):
            self.input_file = input_file
        else:
            raise NameError('input_file does not have a valid type. Please enter the file path or its bytes')
                
        # self.input_file = input_file
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
            j_object = self.jvJRLoader.loadObject(self.ByteArrayInputStream(self.input_file))
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
                self.jasper_design = self.JRXmlLoader.load(self.ByteArrayInputStream(self.input_file))
                self.initial_input_type = 'JASPER_DESIGN'
                self.compile()
            except Exception as ex:
                raise NameError('input file: {0} is not a valid jrxml file:'.format(str(ex)))

        self.jasper_subreports = {}
        for subreport_name, subreport_file in self.config.subreports.items():
            try:
                with open(subreport_file, 'rb') as subreport_file_bytes:
                    subreport_jasper_design = self.JRXmlLoader.load(self.ByteArrayInputStream(subreport_file_bytes.read()))
                    ext_sub_report = os.path.splitext(subreport_file)[-1]
                    sub_report_without_ext = os.path.splitext(subreport_file)[0]
                    jasper_file_subreport = str(sub_report_without_ext) + '.jasper'
                    if ext_sub_report == '.jrxml':
                        print("Compiling: {}".format(subreport_file))
                        self.jvJasperCompileManager.compileReportToFile(subreport_file, jasper_file_subreport)                    
                    self.jasper_subreports[subreport_name] = self.jvJasperCompileManager.compileReport(subreport_jasper_design)
            except Exception:
                raise NameError('input file: {0} is not a valid jrxml file'.format(subreport_name))        

    def compile(self):
        # TODO: Avoid WARNING at first loading when compiling design into report.
        # Illegal reflective access by net.sf.jasperreports.engine.util.ClassUtils
        # to constructor com.sun.org.apache.xerces.internal.util.XMLGrammarPoolImpl()
        self.jasper_report = self.jvJasperCompileManager.compileReport(self.jasper_design)
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
            if isinstance(self.config.params[key], dict):
                param_dict = self.config.params[key]
                type_var = param_dict.get('type')
                if isinstance(type_var, self.TypeJava):
                    type_instance_java = type_var.value
                    type_name = type_var.name
                    if type_instance_java:
                        if type_name == 'BigInteger':
                            value_java = jpype.JClass(type_instance_java)(str(param_dict.get('value')))
                        
                        elif type_name == 'Array':
                            list_values = param_dict.get('value')
                            first_val = list_values[0]
                            if type(first_val) == int:
                                IntArrayCls = JArray(JInt)
                                int_array = IntArrayCls(list_values)
                                value_java = int_array
                            elif type(first_val) == str:
                                StrArrayCls = JArray(JString)
                                str_array = StrArrayCls(list_values)
                                value_java = str_array 
                            else:
                                raise NameError('Array type only accepts Int and Str')
                        elif type_name == 'ArrayList':
                            from java.util import ArrayList # pyright: ignore[reportMissingImports]
                            value_java = ArrayList()
                            list_values = param_dict.get('value')
                            for itm in list_values:
                                if type(itm) == int:
                                    value_java.add(JInt(itm))
                                elif type(itm) == str:
                                    value_java.add(JString(itm))
                                elif type(itm) == bool:
                                    value_java.add(JBoolean(itm))
                                elif type(itm) == float:
                                    value_java.add(JFloat(itm))
                                else:
                                    raise NameError('ArrayList type only accepts int, str, bool and float')
                        elif type_name == 'String':
                            value_java = jpype.JClass(type_instance_java)(param_dict.get('value'))
                        elif type_name == 'Integer':
                            value_java = jpype.JClass(type_instance_java)(str(param_dict.get('value')))
                        elif type_name == 'Boolean':
                            if not isinstance(param_dict.get('value'), bool):
                                raise NameError('The value of the name parameter {} is not of type bool'.format(key))
                            value_java = jpype.JClass(type_instance_java)(param_dict.get('value'))
                        elif type_name == 'Float':
                            if not isinstance(param_dict.get('value'), float):
                                raise NameError('The value of the name parameter {} is not of type float'.format(key))
                            value_java = jpype.JClass(type_instance_java)(param_dict.get('value'))
                        elif type_name == 'Date':                          
                            from java.util import Calendar, Date # pyright: ignore[reportMissingImports]
                            from java.text import DateFormat, SimpleDateFormat # pyright: ignore[reportMissingImports]
                            
                            format_in = param_dict.get('format_input', 'yyyy-MM-dd') # Ex.: "dd/MM/yyyy"
                            sdf = SimpleDateFormat(format_in)
                            value_java = sdf.parse(param_dict.get('value')) # Output of type: java.util.Date
                        parameters.put(key, value_java)
                    else:
                        raise NameError('Instance JAVA not locate')                    
                else:
                    print('{} parameter does not have an TypeJava type'.format(key))
            else:
                parameters.put(key, self.config.params[key])
            
        # /!\ NOTE: Sub-reports are loaded after params to avoid them to be override
        for subreport_key, subreport in self.jasper_subreports.items():
            parameters.put(subreport_key, subreport)
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
                if self.config.jsonLocale:
                    ds.setLocale(self.LocaleUtils.toLocale(self.config.jsonLocale))
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

    def get_output_stream_pdf(self):
        output_stream = self.ByteArrayOutputStream()
        self.JasperExportManager.exportReportToPdfStream(self.jasper_print, output_stream)
        return output_stream

    def fetch_pdf_report(self):
        output_stream_pdf = self.get_output_stream_pdf()
        return output_stream_pdf.toByteArray()
    

    def export_pdf(self):
        output_stream = self.get_output_stream('.pdf')
        output_stream_pdf = self.get_output_stream_pdf()
        output_stream_pdf.writeTo(output_stream)
        output_stream_pdf.flush() # if no buffer used, it can be ignored.
        output_stream_pdf.close()       

    def export_html(self):
        exporter = self.HtmlExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        output_stream = self.SimpleHtmlExporterOutput(self.get_output_stream(".html"))
        exporter.setExporterOutput(output_stream)
        exporter.exportReport()

    def export_rtf(self):
        exporter = self.JRRtfExporter()
        exporter.setExporterInput(self.SimpleExporterInput(self.jasper_print))
        exporter.setExporterOutput(self.SimpleWriterExporterOutput(self.get_output_stream('.rtf')))
        exporter.exportReport()

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

