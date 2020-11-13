# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
from unittest import TestCase
import warnings
from pyreportjasper import PyReportJasper


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            warnings.simplefilter("ignore", DeprecationWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestJasperPy(TestCase):
    EXAMPLES_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'examples')

    @ignore_warnings
    def setUp(self):
        self.input_file = os.path.join(self.EXAMPLES_DIR, 'hello_world.jrxml')
        self.jasper = PyReportJasper()

    @ignore_warnings
    def test_compile(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_process(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_subreports(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_jsonql(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_json_process(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_json_url(self):
        # TODO: To implement
        pass

    @ignore_warnings
    def test_csv(self):
        # TODO: To implement
        pass