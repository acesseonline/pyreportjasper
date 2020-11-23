# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
import warnings
from unittest import TestCase
from pyreportjasper import PyReportJasper


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestPyReportJasper(TestCase):
    RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'test', 'resources')

    def get_config_csv(self):
        db_connection = {
            'driver': 'csv',
            'data_file': os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv'),
            'csv_charset': 'utf-8',
            'csv_out_charset': 'utf-8',
            'csv_field_del': '|',
            'csv_out_field_del': '|',
            'csv_record_del': "\r\n",
            'csv_first_row': True,
            'csv_columns': "Name,Street,City,Phone".split(",")
        }
        return db_connection

    @ignore_warnings
    def setUp(self):
        self.pyreportjasper = PyReportJasper()

    @ignore_warnings
    def test_deprecated_export_pdf(self):
        with self.assertWarns(DeprecationWarning) as cm:
            input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
            output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'deprecated_compile_to_file')
            self.pyreportjasper.process(
                input_file,
                output_file,
                format_list=["pdf"],
                db_connection=self.get_config_csv()
            )
        the_warning = cm.warning
        self.assertEqual(the_warning.args[0], 'process is deprecated - use config and then process_report instead. '
                                              'See the documentation https://pyreportjasper.readthedocs.io')
        self.assertEqual(os.path.isfile(output_file + '.pdf'), True)

    @ignore_warnings
    def test_compile_to_file(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithStudioBuiltinFunctions.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_studio_builtin_functions2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_javascript(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_javascript(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'charactersetTestWithJavaScript.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'characterset_test_with_javascript2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_compile_to_file_jasperreports_functions2(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'Blank_A4_1.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'blank_A4_1_2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_export_pdf(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["pdf"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.pdf'), True)

    @ignore_warnings
    def test_export_rtf(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["rtf"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.rtf'), True)

    @ignore_warnings
    def test_export_docx(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["docx"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.docx'), True)

    @ignore_warnings
    def test_export_odt(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["odt"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.odt'), True)

    @ignore_warnings
    def test_export_xml(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["xml"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.xml'), True)
    #
    @ignore_warnings
    def test_export_xls(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["xls"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.xls'), True)

    @ignore_warnings
    def test_export_xlsx(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["xlsx"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.xlsx'), True)

    @ignore_warnings
    def test_export_csv(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["csv"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        output_file = output_file + '.csv'
        self.assertEqual(os.path.isfile(output_file), True)
        with open(output_file, 'r') as f:
            rows = f.readlines()
            self.assertEqual(rows[2], '|Name|Street||City|Phone|\n')

    @ignore_warnings
    def test_export_csv_meta(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csvMeta2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["csv_meta"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        output_file = output_file + '.csv'
        self.assertEqual(os.path.isfile(output_file), True)
        with open(output_file, 'r') as f:
            rows = f.readlines()
            self.assertEqual(rows[2], "Carl Grant|Ap #507-5431 Consectetuer, Avenue|Chippenham|1-472-350-4152\n")

    @ignore_warnings
    def test_export_ods(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["ods"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.ods'), True)

    @ignore_warnings
    def test_export_pptx(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'csv.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'compile_to_file2')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["pptx"],
            db_connection=self.get_config_csv()
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.pptx'), True)

    @ignore_warnings
    def test_get_report_parameters(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'noDB-params.jrxml')
        self.pyreportjasper.config(
            input_file,
            output_formats=["xlsx"],
            db_connection=self.get_config_csv()
        )
        result = self.pyreportjasper.list_report_params()
        self.assertEqual(str(result[-4]), "myString")
        self.assertEqual(str(result[-3]), "myInt")
        self.assertEqual(str(result[-2]), "myDate")
        self.assertEqual(str(result[-1]), "myImage")

    @ignore_warnings
    def test_fill_from_xml_datasource(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'CancelAck.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'cancel_ack2')
        data_file = os.path.join(self.RESOURCES_DIR, 'CancelAck.xml')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'xml',
                'data_file': data_file,
                'xml_xpath': '/CancelResponse/CancelResult/ID',
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_xml_datasource_no_xpath(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'CancelAck.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'cancel_ack_no_xpath2')
        data_file = os.path.join(self.RESOURCES_DIR, 'CancelAck.xml')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'xml',
                'data_file': data_file
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_json_datasource(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'json.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'json2')
        data_file = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'json',
                'data_file': data_file,
                'json_query': 'contacts.person'
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_json_datasource_no_json_query(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'json.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'json_no_query2')
        data_file = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'json',
                'data_file': data_file,
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_jsonql_datasource(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql2')
        data_file = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'jsonql',
                'data_file': data_file,
                'json_query': 'contacts.person'
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_jsonql_datasource_no_jsonql_query(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'jsonql_no_query2')
        data_file = os.path.join(self.RESOURCES_DIR, 'contacts.json')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'jsonql',
                'data_file': data_file,
                'json_query': 'contacts.person'
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_fill_from_xml_barcode4j(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j_2')
        data_file = os.path.join(self.RESOURCES_DIR, 'barcode4j.xml')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["jrprint"],
            db_connection={
                'driver': 'xml',
                'data_file': data_file,
                'xml_xpath': '/nalepka/ident'
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.jrprint'), True)

    @ignore_warnings
    def test_export_pdf_barcode4j(self):
        input_file = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j.jrxml')
        output_file = os.path.join(self.RESOURCES_DIR, 'reports', 'barcode4j_2')
        data_file = os.path.join(self.RESOURCES_DIR, 'barcode4j.xml')
        self.pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["pdf"],
            db_connection={
                'driver': 'xml',
                'data_file': data_file,
                'xml_xpath': '/nalepka/ident'
            }
        )
        self.pyreportjasper.process_report()
        self.assertEqual(os.path.isfile(output_file + '.pdf'), True)
