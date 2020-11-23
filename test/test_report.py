# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
from unittest import TestCase
import warnings
from pyreportjasper.config import Config
from pyreportjasper.report import Report


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            warnings.simplefilter("ignore", DeprecationWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestReport(TestCase):
    RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'test', 'resources')

    def get_config_csv(self):
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
        return config

    @ignore_warnings
    def setUp(self):
        pass

    @ignore_warnings
    def test_compile_to_file(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithStudioBuiltinFunctions.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_studio_builtin_functions')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_javascript(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_javascript(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions2(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'Blank_A4_1.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'blank_A4_1')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_export_pdf(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_pdf()
        self.assertEqual(os.path.isfile(config.output + '.pdf'), True)

    @ignore_warnings
    def test_export_rtf(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_rtf()
        self.assertEqual(os.path.isfile(config.output + '.rtf'), True)

    @ignore_warnings
    def test_export_docx(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_docx()
        self.assertEqual(os.path.isfile(config.output + '.docx'), True)

    @ignore_warnings
    def test_export_odt(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_odt()
        self.assertEqual(os.path.isfile(config.output + '.odt'), True)

    @ignore_warnings
    def test_export_xml(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xml()
        self.assertEqual(os.path.isfile(config.output + '.xml'), True)

    @ignore_warnings
    def test_export_xls(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xls()
        self.assertEqual(os.path.isfile(config.output + '.xls'), True)

    @ignore_warnings
    def test_export_xlsx(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_xlsx()
        self.assertEqual(os.path.isfile(config.output + '.xlsx'), True)

    @ignore_warnings
    def test_export_csv(self):
        config = self.get_config_csv()
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
        config = self.get_config_csv()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta')
        instance = Report(config, config.input)
        instance.fill()
        instance.export_csv_meta()
        output_file = config.output + '.csv'
        self.assertEqual(os.path.isfile(output_file), True)
        with open(output_file, 'r') as f:
            rows = f.readlines()
            self.assertEqual(rows[2], "Carl Grant|Ap #507-5431 Consectetuer, Avenue|Chippenham|1-472-350-4152\n")

    @ignore_warnings
    def test_export_ods(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_ods()
        self.assertEqual(os.path.isfile(config.output + '.ods'), True)

    @ignore_warnings
    def test_export_pptx(self):
        config = self.get_config_csv()
        instance = Report(config, config.input)
        instance.fill()
        instance.export_pptx()
        self.assertEqual(os.path.isfile(config.output + '.pptx'), True)

    @ignore_warnings
    def test_get_report_parameters(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'noDB-params.jrxml')
        instance = Report(config, config.input)
        result = instance.get_report_parameters()

        self.assertEqual(str(result[result.length - 4].getName()), "myString")
        self.assertEqual(str(result[result.length - 3].getName()), "myInt")
        self.assertEqual(str(result[result.length - 2].getName()), "myDate")
        self.assertEqual(str(result[result.length - 1].getName()), "myImage")

    @ignore_warnings
    def test_fill_from_xml_datasource(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'CancelAck.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'cancel_ack')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'CancelAck.xml')
        config.dbType = 'xml'
        config.xmlXpath = '/CancelResponse/CancelResult/ID'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_xml_datasource_no_xpath(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'CancelAck.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'cancel_ack_no_xpath')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'CancelAck.xml')
        config.dbType = 'xml'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_json_datasource(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'json.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'json')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        config.dbType = 'json'
        config.jsonQuery = 'contacts.person'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_json_datasource_no_json_query(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'json.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'json_no_query')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        config.dbType = 'json'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_jsonql_datasource(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        config.dbType = 'jsonql'
        config.jsonQuery = 'contacts.person'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_jsonql_datasource_no_jsonql_query(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql_no_query')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        config.dbType = 'jsonql'
        config.jsonQuery = 'contacts.person'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_xml_barcode4j(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'barcode4j.xml')
        config.dbType = 'xml'
        config.xmlXpath = '/nalepka/ident'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_jrprint()
        self.assertEqual(os.path.isfile(config.output + '.jrprint'), True)

    @ignore_warnings
    def test_export_pdf_barcode4j(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j.jrxml')
        config.output = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j')
        config.dataFile = os.path.join(self.RESOURCES_DIR, 'barcode4j.xml')
        config.dbType = 'xml'
        config.xmlXpath = '/nalepka/ident'
        instance = Report(config, config.input)
        instance.fill()
        instance.export_pdf()
        self.assertEqual(os.path.isfile(config.output + '.pdf'), True)

    @ignore_warnings
    def test_get_main_dataset_query_from_xml(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'CancelAck.jrxml')
        instance = Report(config, config.input)
        dataset_query = instance.get_main_dataset_query()
        self.assertEqual(dataset_query, '/CancelResponse/CancelResult/ID')

    @ignore_warnings
    def test_get_main_dataset_query_from_json(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'json.jrxml')
        instance = Report(config, config.input)
        dataset_query = instance.get_main_dataset_query()
        self.assertEqual(dataset_query, 'contacts.person')

    @ignore_warnings
    def test_get_main_dataset_query_from_jsonql(self):
        config = Config()
        config.input = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql.jrxml')
        instance = Report(config, config.input)
        dataset_query = instance.get_main_dataset_query()
        self.assertEqual(dataset_query, 'contacts.person')