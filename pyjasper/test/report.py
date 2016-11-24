# -*- coding: utf-8 -*-
import sys
import os
from platform import python_version
sys.path.insert(0,'../..')
import pyjasper


def compiling():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world.jrxml'	
	jasper = pyjasper.JasperPy()
	jasper.compile(input).execute()


def processing():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world.jrxml'
	output = os.path.dirname(os.path.abspath(__file__)) + '/output/exemples'
	jasper = pyjasper.JasperPy()
	jasper.process(input, output, ["pdf","rtf"]).execute()


def listingParameters():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world_params.jrxml'
	jasper = pyjasper.JasperPy()
	output = jasper.list_parameters(input).execute()	
	print(output)


def advancedExampleUsingDatabase():	
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world.jrxml'
	output = os.path.dirname(os.path.abspath(__file__)) + '/output/exemples'
	con = {
        'driver' : 'postgres',
        'username' : 'DB_USERNAME',
        'password' : 'DB_PASSWORD',
        'host' : 'DB_HOST',
        'database' : 'DB_DATABASE',
        'schema' : 'DB_SCHEMA',
        'port' : '5432'		
	}
	jasper = pyjasper.JasperPy()
	jasper.process(
		input,
		output,
		["pdf", "rtf", "xml"],
		{'python_version': python_version()},
		con,
		'pt_BR' # LOCALE Ex.:(en_US, de_GE)
	).execute()	


def xmlToPdf():	
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/CancelAck.jrxml'
	output = os.path.dirname(os.path.abspath(__file__)) + '/output/_CancelAck'
	dataFile = os.path.dirname(os.path.abspath(__file__)) + '/exemples/CancelAck.xml'
	drive = 'xml'
	xmlXpath = '/CancelResponse/CancelResult/ID'
	jasper = pyjasper.JasperPy()
	jasper.process(
		input,
		output,
		["pdf"],
		{},
		{'data_file':dataFile, 'driver':drive, 'xml_xpath':xmlXpath},
		'pt_BR' # LOCALE Ex.:(en_US, de_GE)
	).execute()	
	print('Result is the file below.')
	print(output+'.pdf')


def jsonToPdf():	
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/json.jrxml'
	output = os.path.dirname(os.path.abspath(__file__)) + '/output/_Contacts'
	json_query = 'contacts.person'
	dataFile = os.path.dirname(os.path.abspath(__file__)) + '/exemples/contacts.json'
	jasper = pyjasper.JasperPy()
	jasper.process(
		input,
		output,
		["pdf"],
		{},
		{'data_file':dataFile, 'driver':'json', 'json_query':json_query},
		'pt_BR' # LOCALE Ex.:(en_US, de_GE)
	).execute()
	print('Result is the file below.')
	print(output+'.pdf')

jsonToPdf()	