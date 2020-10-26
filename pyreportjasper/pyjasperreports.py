# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 David Lehrian <david@lehrian.com>
#

import os
import jpyutil
        
class PyJasperReports:
    connection = None
    config = None

    def __init__(self, resource_dir=False, jvm_maxmem='512M', jvm_classpath=None):
        self.WINDOWS = True if os.name == 'nt' else False
        self.SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
        self.LIBS = os.path.join(self.SCRIPT_DIR, 'jasperstarter', 'lib')
        if not os.path.isdir(self.LIBS):
            raise NameError('Unable to find lib in {0}'.format(self.LIBS))
        self.CLASSPATH = os.path.join(self.LIBS, 'jasperstarter.jar')
        if not os.path.exists(self.CLASSPATH):
            raise NameError('Unable to find jasperstarter in {0}'.format(self.LIBS))
        if jvm_classpath is None:
            jpyutil.init_jvm(jvm_maxmem=jvm_maxmem, jvm_classpath=[self.CLASSPATH])
        else:
            jpyutil.init_jvm(jvm_maxmem=jvm_maxmem, jvm_classpath=[self.CLASSPATH, jvm_classpath])
            
        # IMPORT jpy HERE AFTER init_jvm
        import jpy
        self.jvStringBuilder = jpy.get_type('java.lang.StringBuilder')
        self.jvHashMap = jpy.get_type('java.util.HashMap')

        self.jvJasperFillManager = jpy.get_type('net.sf.jasperreports.engine.JasperFillManager')
        self.jvJasperCompileManager = jpy.get_type('net.sf.jasperreports.engine.JasperCompileManager')
        self.jvSimpleHtmlExporterOutput = jpy.get_type('net.sf.jasperreports.export.SimpleHtmlExporterOutput')
        self.jvHtmlExporter = jpy.get_type('net.sf.jasperreports.engine.export.HtmlExporter')
        self.jvJRPdfExporter = jpy.get_type('net.sf.jasperreports.engine.export.JRPdfExporter')
        self.jvJRXlsExporter = jpy.get_type('net.sf.jasperreports.engine.export.JRXlsExporter')
        self.jvJRXmlExporter = jpy.get_type('net.sf.jasperreports.engine.export.JRXmlExporter')
        self.jvJRCsvExporter = jpy.get_type('net.sf.jasperreports.engine.export.JRCsvExporter')
        self.jvJRDocxExporter = jpy.get_type('net.sf.jasperreports.engine.export.ooxml.JRDocxExporter')
        self.jvSimpleExporterInput = jpy.get_type('net.sf.jasperreports.export.SimpleExporterInput')
        self.jvSimpleHtmlReportConfiguration = jpy.get_type('net.sf.jasperreports.export.SimpleHtmlReportConfiguration')
        self.jvWebHtmlResourceHandler = jpy.get_type('net.sf.jasperreports.web.util.WebHtmlResourceHandler')
        self.jvSimpleOutputStreamExporterOutput = jpy.get_type('net.sf.jasperreports.export.SimpleOutputStreamExporterOutput')
        self.jvSimpleWriterExporterOutput = jpy.get_type('net.sf.jasperreports.export.SimpleWriterExporterOutput')
        self.jvSimpleXmlExporterOutput = jpy.get_type('net.sf.jasperreports.export.SimpleXmlExporterOutput')
        self.jvJRSaver = jpy.get_type('net.sf.jasperreports.engine.util.JRSaver')
        self.jvJRLoader = jpy.get_type('net.sf.jasperreports.engine.util.JRLoader')
        
        self.jvDsType = jpy.get_type('de.cenote.jasperstarter.types.DsType')
        self.jvDb = jpy.get_type('de.cenote.jasperstarter.Db')
        self.jvConfig = jpy.get_type('de.cenote.jasperstarter.Config')
        self.jvApplicationClasspath = jpy.get_type('de.cenote.tools.classpath.ApplicationClasspath')
        self.jvApplicationClasspath.addJarsRelative('../jdbc')

        self.path_executable = os.path.dirname(os.path.abspath(__file__)) \
                               + '/jasperstarter/bin'
        self.windows = True if os.name == 'nt' else False
        self._command = ''

        if not resource_dir:
            resource_dir = os.path.dirname(os.path.abspath(__file__)) \
                           + '/jasperstarter/bin'
        else:
            if not os.path.exists(resource_dir):
                raise NameError('Invalid resource directory!')

        self.resource_directory = resource_dir
        
        
    def compile(self, input_file, output_file=False):
        jr = self.jvJasperCompileManager.compileReport(input_file)
        if output_file:
            base = os.path.splitext(input_file)[0]
            self.jvJRSaver.saveObject(jr, base + ".jasper");
        return jr

    def load(self, jasper_file):
        return self.jvJRLoader.loadObjectFromFile(jasper_file)

    def fill(self, jr,parametersDict, connectionDict):
        if self.connection is None:
            self.config = self.jvConfig()
            for key in connectionDict:
                method = getattr(self, key)
                method(connectionDict[key])
                                
            jvDb = self.jvDb()
            self.connection = jvDb.getConnection(self.config)
        parametersMap = self.jvHashMap()
        for key in parametersDict:
            parametersMap.put(key,parametersDict[key])
        jasperPrint = self.jvJasperFillManager.fillReport(jr,parametersMap,self.connection)
        return jasperPrint
    
    def askFilter(self,value):
        self.config.setAskFilter(value)
    def command(self,value):
        self.config.setCommand(value)
    def dbDriver(self,value):
        self.config.setDbDriver(value)
    def dbHost(self,value):
        self.config.setDbHost(value)
    def dbName(self,value):
        self.config.setDbName(value)
    def dbPasswd(self,value):
        self.config.setDbPasswd(value)
    def dbPort(self,value):
        self.config.setDbPort(value)
    def dbSid(self,value):
        self.config.setDbSid(value)
    def dbType(self,value):
        self.config.setDbType(self.jvDsType.valueOf(value))
    def dbUrl(self,value):
        self.config.setDbUrl(value)
    def dbUser(self,value):
        self.config.setDbUser(value)

    # this method returns an HTML string that is the report  DML 10/26/2020
    def generateHtml(self, jasperPrint, outputFile,imageUrl):
        # create the output directory DML 10/25/2020
        if not os.path.exists(os.path.dirname(outputFile)):
            os.makedirs(os.path.dirname(outputFile))
        # create an HtmlExporter and set the jasperPrint object as the input  DML 10/26/2020
        exporter = self.jvHtmlExporter()
        exporterInput = self.jvSimpleExporterInput(jasperPrint);
        exporter.setExporterInput(exporterInput)
        # set a few configuration values to not set the page background as white, leave it as the CSS has it set,
        # and remove empty space between rows.  DML 10/26/2020
        reportExportConfiguration = self.jvSimpleHtmlReportConfiguration()
        reportExportConfiguration.setWhitePageBackground(False)
        reportExportConfiguration.setRemoveEmptySpaceBetweenRows(True)
        exporter.setConfiguration(reportExportConfiguration)
        # this sets the output of the exporter to be a SimpleHtmlExporterOutput to the outputFile.  This is done
        # solely to get any graph objects that are generated as png files during the creation of the report
        # to save to disk so they can be referenced in the HTML output via the imageUrl and the WebHtmlResourceHandler
        # a few lines below   DML 10/26/2020
        exporterOutput = self.jvSimpleHtmlExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        # Delete the generated HTML file because it isn't necessary. It is only generated so we get the
        # graph images written to disk so they can be included in the report. DML 10/26/2020
        os.remove(outputFile)
        # this sets the output of the SimpleHtmlExporterOutput to a StringBuilder  DML 10/26/2020
        sbuilder = self.jvStringBuilder()
        exporterOutput = self.jvSimpleHtmlExporterOutput(sbuilder)
        # set the URL to the images that get saved when the exporter is run with the outputFile  DML 10/26/2020
        exporterOutput.setImageHandler(self.jvWebHtmlResourceHandler(imageUrl + "{0}"))
        # set the exporterOutput to the sbuilder and export it.  DML 10/26/202
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        # return the sbuilder toString value  DML 10/26/2020
        return sbuilder.toString()

    def generatePdf(self,jasperPrint,outputFile):
        exporter = self.jvJRPdfExporter()
        exporter.setExporterInput(self.jvSimpleExporterInput(jasperPrint))
        exporterOutput = self.jvSimpleOutputStreamExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        
    def generateXls(self,jasperPrint,outputFile):
        exporter = self.jvJRXlsExporter()
        exporter.setExporterInput(self.jvSimpleExporterInput(jasperPrint))
        exporterOutput = self.jvSimpleOutputStreamExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        
    def generateCsv(self,jasperPrint,outputFile):
        exporter = self.jvJRCsvExporter()
        exporter.setExporterInput(self.jvSimpleExporterInput(jasperPrint))
        exporterOutput = self.jvSimpleWriterExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        
    def generateDocx(self,jasperPrint,outputFile):
        exporter = self.jvJRDocxExporter()
        exporter.setExporterInput(self.jvSimpleExporterInput(jasperPrint))
        exporterOutput = self.jvSimpleOutputStreamExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        
    def generateXml(self,jasperPrint,outputFile):
        exporter = self.jvJRXmlExporter()
        exporter.setExporterInput(self.jvSimpleExporterInput(jasperPrint))
        exporterOutput = self.jvSimpleXmlExporterOutput(outputFile)
        exporter.setExporterOutput(exporterOutput)
        exporter.exportReport()
        