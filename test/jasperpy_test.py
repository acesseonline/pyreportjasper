# -*- coding: utf-8 -*-
import os
from unittest import TestCase
from pyjasper.jasperpy import JasperPy


class TestJasperPy(TestCase):

    def setUp(self):
        self.input_file = os.path.dirname(os.path.abspath(__file__)) \
                     + '/examples/hello_world.jrxml'

        self.jasper = JasperPy()

    def test_compile(self):
        self.assertRaises(NameError, self.jasper.compile, False)
        self.assertEqual(self.jasper.compile(self.input_file), 0)

    def test_process(self):
        self.assertRaises(NameError, self.jasper.process, False)

        kwargs = {
            'input_file': self.input_file,
            'format_list': 'pdf'
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        kwargs = {
            'input_file': self.input_file,
            'format_list': 5
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        kwargs = {
            'input_file': self.input_file,
            'format_list': ['mp3']
        }
        self.assertRaises(NameError, self.jasper.process, **kwargs)

        self.assertEqual(self.jasper.process(self.input_file), 0)

    def test_list_parameters(self):
        self.assertRaises(NameError, self.jasper.list_parameters, False)
        self.assertEqual(self.jasper.list_parameters(self.input_file), 0)

    def test_execute(self):
        self.assertEqual(self.jasper.execute(), 0)

        self.jasper.path_executable = ''
        self.assertRaises(NameError, self.jasper.execute, False)
