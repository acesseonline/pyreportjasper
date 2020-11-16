# -*- coding: utf-8 -*-

"""
ATTENTION: This file is only for testing during development, after which it will be deleted.
"""


import os
from pyreportjasper import PyReportJasper

examples_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples')
input_file = os.path.join(examples_dir, 'json.jrxml')
data_file = os.path.join(examples_dir, 'contacts.json')
pyreportjasper = PyReportJasper()
pyreportjasper.set_up(
    input_file,
    output_formats=["pdf"],
    parameters={},
    db_connection={
        'data_file': data_file,
        'driver': 'json',
        'json_query': 'contacts.person',
        'json_locale': 'es_ES',
        'json_date_pattern': 'yyyy-MM-dd',
        'json_number_pattern': '#,##0.##'
    },
    locale='en_US'  # LOCALE Ex.:(pt_BR, de_GE)
)
pyreportjasper.compile()
pyreportjasper.process_report()
# pyreportjasper.list_report_params()

