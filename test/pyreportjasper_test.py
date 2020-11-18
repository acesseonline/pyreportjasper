# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
from unittest import TestCase
import warnings
from pyreportjasper import PyReportJasper
from pyreportjasper.config import Config
from pyreportjasper.report import Report


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            warnings.simplefilter("ignore", DeprecationWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestPyReportJasper(TestCase):
    RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'test', 'resources')

    @ignore_warnings
    def setUp(self):
        self.input_file = os.path.join(self.RESOURCES_DIR, 'hello_world.jrxml')
        self.pyreportjasper = PyReportJasper()

    @ignore_warnings
    def test_compile_to_file(self):
        print('compile_to_file')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        instance = Report(config, config.input)
        instance.compile_to_file()
        self.assertEqual(os.path.isfile(config.output + '.jasper'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions(self):
        print('compile_to_file_jasperreports_functions')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithStudioBuiltinFunctions.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_studio_builtin_functions')
        instance = Report(config, config.input)
        instance.compile_to_file()
        self.assertEqual(os.path.isfile(config.output + '.jasper'), True)

    @ignore_warnings
    def test_compile_to_file_javascript(self):
        print('compile_to_file_javascript')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript')
        instance = Report(config, config.input)
        instance.compile_to_file()
        self.assertEqual(os.path.isfile(config.output + '.jasper'), True)

    @ignore_warnings
    def test_fill_javascript(self):
        print('fill_javascript')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript')
        instance = Report(config, config.input)
        instance.compile_to_file()
        self.assertEqual(os.path.isfile(config.output + '.jasper'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions2(self):
        print('compile_to_file_jasperreports_functions2')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'Blank_A4_1.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'blank_A4_1')
        instance = Report(config, config.input)
        instance.compile_to_file()
        self.assertEqual(os.path.isfile(config.output + '.jasper'), True)

    @ignore_warnings
    def test_export_pdf(self):
        print('export pdf')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_pdf()
        self.assertEqual(os.path.isfile(config.output + '.pdf'), True)

    @ignore_warnings
    def test_export_rtf(self):
        print('export rtf')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_rtf()
        self.assertEqual(os.path.isfile(config.output + '.rtf'), True)

    @ignore_warnings
    def test_export_docx(self):
        print('export docx')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_docx()
        self.assertEqual(os.path.isfile(config.output + '.docx'), True)

    @ignore_warnings
    def test_export_odt(self):
        print('export odt')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_odt()
        self.assertEqual(os.path.isfile(config.output + '.odt'), True)

    @ignore_warnings
    def test_export_html(self):
        print('export html')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_html()
        self.assertEqual(os.path.isfile(config.output + '.html'), True)

    @ignore_warnings
    def test_export_xml(self):
        print('export xml')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xml()
        self.assertEqual(os.path.isfile(config.output + '.xml'), True)

    @ignore_warnings
    def test_export_xls(self):
        print('export xls')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xls()
        self.assertEqual(os.path.isfile(config.output + '.xls'), True)

    @ignore_warnings
    def test_export_xlsx(self):
        print('export xlsx')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.csvFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xlsx()
        self.assertEqual(os.path.isfile(config.output + '.xlsx'), True)

    @ignore_warnings
    def test_export_csv(self):
        print('export csv')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.outCharset = "utf-8"
        config.csvFieldDel = "|"
        config.outFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_csv()
        output_file = config.output + '.csv'
        self.assertEqual(os.path.isfile(output_file), True)
        with open(output_file, 'r') as f:
            rows = f.readlines()
            self.assertEqual(rows[2], '|Name|Street||City|Phone|\n')

    @ignore_warnings
    def test_export_csv_meta(self):
        print('export csv meta')
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv')
        config.dbType = 'csv'
        config.csvCharset = "utf-8"
        config.outCharset = "utf-8"
        config.csvFieldDel = "|"
        config.outFieldDel = "|"
        config.csvRecordDel = "\r\n"
        config.csvFirstRow = True
        config.csvColumns = "Name,Street,City,Phone".split(",")
        instance = Report(config, config.input)
        instance.fill()
        instance.export_csv_meta()
        output_file = config.output + '.csv'
        self.assertEqual(os.path.isfile(output_file), True)
        with open(output_file, 'r') as f:
            rows = f.readlines()
            print(rows[2])
            self.assertEqual(rows[2], "Carl Grant|Ap #507-5431 Consectetuer, Avenue|Chippenham|1-472-350-4152\n")