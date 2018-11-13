# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2017 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#
import os
from unittest import TestCase
from pyreportjasper import JasperPy


class TestJasperPy(TestCase):

    def setUp(self):
        self.input_file = 'examples/hello_world.jrxml'
        self.jasper = JasperPy()

    def test_compile(self):
        self.assertRaises(NameError, self.jasper.compile, False)
        self.assertEqual(self.jasper.compile(self.input_file), 0)

    def test_process(self):
        self.assertRaises(NameError, self.jasper.process, False)

        # test invalid format input. Must be list ['pdf']
        kwargs = {
            'input_file': self.input_file,
            'format_list': 'pdf'
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        # test invalid input format
        kwargs = {
            'input_file': self.input_file,
            'format_list': 5
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        # test invalid report format
        kwargs = {
            'input_file': self.input_file,
            'format_list': ['mp3']
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        # test
        self.assertEqual(
            self.jasper.process(self.input_file,
                                format_list=['pdf', 'odt', 'xls']), 0)

    def test_list_parameters(self):
        self.input_file = 'examples/hello_world_params.jrxml'
        self.assertRaises(NameError, self.jasper.list_parameters, False)
        self.assertEqual(self.jasper.list_parameters(self.input_file),
                         {
                             'myString': ['java.lang.String', ''],
                             'myInt': ['java.lang.Integer', ''],
                             'myDate': ['java.util.Date', ''],
                             'myImage': ['java.awt.Image',
                                         'This is the description'
                                         ' of parameter myImage']
                         })

    def test_execute(self):
        self.assertEqual(self.jasper.execute(), 0)

        self.jasper.path_executable = ''
        self.assertRaises(NameError, self.jasper.execute, False)


    def test_subreports(self):
        input_file_header = 'examples/subreports/header.jrxml'

        input_file_details = 'examples/subreports/details.jrxml'

        input_file_main = 'examples/subreports/main.jrxml'

        self.input_file = 'examples/subreports/main.jasper'

        data_file = 'examples/subreports/contacts.xml'


        self.jasper.compile(input_file_header)
        self.jasper.compile(input_file_details)
        self.jasper.compile(input_file_main)

        self.assertEqual(
            self.jasper.process(
                self.input_file,
                format_list=["pdf"],
                parameters={},
                db_connection={
                    'data_file': data_file,
                    'driver': 'xml',
                    'xml_xpath': '"/"',
                },
                locale='pt_BR',  # LOCALE Ex.:(en_US, de_GE)
                resource='examples/subreports/'
            ), 0)

    def test_jsonql(self):
        self.input_file = 'examples/jsonql.jrxml'

        data_file = 'examples/contacts.json'

        self.assertEqual(
            self.jasper.process(
                self.input_file,
                format_list=["pdf"],
                parameters={},
                db_connection={
                    'data_file': data_file,
                    'driver': 'jsonql',
                    'jsonql_query': 'contacts.person',
                },
                locale='pt_BR',  # LOCALE Ex.:(en_US, de_GE)
            ), 0)

