# -*- coding: utf-8 -*-
import sys
import os
from platform import python_version
import pyjasper

sys.path.insert(0, '../..')


def compiling():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    jasper = pyjasper.JasperPy()
    jasper.compile(input_file).execute()


def processing():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file, output=output, format_list=["pdf", "rtf"]).execute()


def listing_parameters():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world_params.jrxml'
    jasper = pyjasper.JasperPy()
    output = jasper.list_parameters(input_file).execute()
    print(output)


def advanced_example_using_database():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    con = {
        'driver': 'postgres',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'host': 'DB_HOST',
        'database': 'DB_DATABASE',
        'schema': 'DB_SCHEMA',
        'port': '5432'
    }
    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file,
        output=output,
        format_list=["pdf", "rtf", "xml"],
        parameters={'python_version': python_version()},
        db_connection=con,
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    ).execute()


def xml_to_pdf():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/CancelAck.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_CancelAck'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/CancelAck.xml'

    jasper = pyjasper.JasperPy()

    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'xml',
            'xml_xpath': '/CancelResponse/CancelResult/ID',
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    ).execute()

    print('Result is the file below.')
    print(output + '.pdf')


def json_to_pdf():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/json.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_Contacts'
    json_query = 'contacts.person'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/contacts.json'

    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'json',
            'json_query': json_query,
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    ).execute()

    print('Result is the file below.')
    print(output + '.pdf')


json_to_pdf()
