# -*- coding: utf-8 -*-
import os
from unittest import TestCase
from pyjasper.jasperpy import JasperPy


class TestJasperPy(TestCase):

    def test_compile(self):

        input_file = os.path.dirname(os.path.abspath(__file__)) \
                + '/examples/hello_world.jrxml'

        jasper = JasperPy()
        self.assertRaises(NameError, jasper.compile, False)
        self.assertEqual(jasper.compile(input_file), 0)

    def test_process(self):

        input_file = os.path.dirname(os.path.abspath(__file__)) \
                     + '/examples/hello_world.jrxml'

        jasper = JasperPy()
        self.assertRaises(NameError, jasper.process, False)

        kwargs = {
            'input_file': input_file,
            'format_list': 'pdf'
        }
        self.assertRaises(NameError, jasper.process, **kwargs)

        kwargs = {
            'input_file': input_file,
            'format_list': 5
        }
        self.assertRaises(NameError, jasper.process, **kwargs)

        kwargs = {
            'input_file': input_file,
            'format_list': ['mp3']
        }
        self.assertRaises(NameError, jasper.process, **kwargs)

        self.assertEqual(jasper.process(input_file), 0)

    def test_list_parameters(self):

        input_file = os.path.dirname(os.path.abspath(__file__)) \
                     + '/examples/hello_world.jrxml'

        jasper = JasperPy()
        self.assertRaises(NameError, jasper.list_parameters, False)
        self.assertEqual(jasper.list_parameters(input_file), 0)

    def test_execute(self):

        jasper = JasperPy()
        self.assertEqual(jasper.execute(), 0)

        jasper.path_executable = ''
        self.assertRaises(NameError, jasper.execute, False)
