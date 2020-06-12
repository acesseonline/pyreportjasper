# -*- coding: utf-8 -*-
import os
from pyreportjasper import JasperPy

def advanced_example_using_database():
    file_name = 'jasper'
    input_file_name = '{}.jrxml'.format(file_name)
    input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), input_file_name)
    con = {
        'driver': 'postgres',
        'username': 'postgres',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'relatorio',
        'port': '5432'
    }
    jasper = JasperPy()
    jasper.process(
        input_file_path,
        format_list=["pdf"],
        parameters={},
        db_connection=con,
        locale='pt_BR'
    )

if __name__ == '__main__':
    advanced_example_using_database()