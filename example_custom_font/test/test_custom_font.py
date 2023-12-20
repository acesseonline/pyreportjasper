# -*- coding: utf-8 -*-
import os
from pyreportjasper import PyReportJasper

def processing():
   REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
   input_file = os.path.join(REPORTS_DIR, 'custom_font.jrxml')
   output_file = os.path.join(REPORTS_DIR, 'output', 'custom_font')
   pyreportjasper = PyReportJasper()
   pyreportjasper.config(
     input_file,
     output_file,
     output_formats=["pdf"]
   )
   pyreportjasper.process_report()
   
processing()