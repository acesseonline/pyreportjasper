# Reports for Python, with JasperReports.

**Is using Linux servers?**

Do not forget to grant permission 777 for the directory where is the package.

##Introduction

This package aims to be a solution to compile and process JasperReports (.jrxml & .jasper files).

###Why?

Did you ever had to create a good looking Invoice with a lot of fields for your great web app or desktop?

I had to, and the solutions out there were not perfect. Generating *HTML* + *CSS* to make a *PDF*? WTF? That doesn't make any sense! :)

Then I found **JasperReports** the best open source solution for reporting.

###What can I do with this?

Well, everything. JasperReports is a powerful tool for **reporting** and **BI**.

**From their website:**

> The JasperReports Library is the world's most popular open source reporting engine. It is entirely written in Java and it is able to use data coming from any kind of data source and produce pixel-perfect documents that can be viewed, printed or exported in a variety of document formats including HTML, PDF, Excel, OpenOffice and Word.

It is recommended using [Jaspersoft Studio](http://community.jaspersoft.com/project/jaspersoft-studio) to build your reports, connect it to your datasource (ex:JSON, XML, MySQL, POSTGRES), loop thru the results and output it to PDF, XLS, DOC, RTF, ODF, etc.

*Some examples of what you can do:*

* Invoices
* Reports
* Listings

Package to generate reports with [JasperReports 6.3.1](http://community.jaspersoft.com/project/jaspersoft-studio/releases) library through [JasperStarter v3](http://jasperstarter.sourceforge.net/) command-line tool.

##Requirements

* Java JDK 1.8
* Pyhton [subprocess.run()](https://docs.python.org/3/library/subprocess.html) function
* [optional] [Mysql Connector](http://dev.mysql.com/downloads/connector/j/) (if you want to use database)
* [optional] [PostgreSQL Connector](https://jdbc.postgresql.org/download.html) (if you want to use database)
* [optional] [Jaspersoft Studio](http://community.jaspersoft.com/project/jaspersoft-studio) (to draw and compile your reports)

###Java

Check if you already have Java installed:

```
$ java -version
java version "1.8.0_101"
Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)
```

If you get:

    command not found: java

Then install it with: (Ubuntu/Debian)

    $ sudo apt-get install default-jdk

To install on: (centOS/Fedora)

    # yum install java-1.8.0-openjdk.x86_64

To install on windows visit the link-> [JDK](http://www.oracle.com/technetwork/pt/java/javase/downloads/jdk8-downloads-2133151.html) and look for the most appropriate version for your system.

Now run the `java -version` again and check if the output is ok.

##Installation

Install [PyPI](https://pypi.python.org/pypi) if you don't have it.
```
pip install pyreportjasper
```

and thats it.

##Examples

###The *Hello World* example.

Go to the examples directory in the root of the package 
Open the `test/exemples/hello_world.jrxml` file with Jaspersoft Studio or with your favorite text editor and take a look at the source code.

#### Compiling

First we need to compile our `JRXML` file into a `JASPER` binary file. We just have to do this one time.

**Note 1:** You don't need to do this step if you are using *Jaspersoft Studio*. You can compile directly within the program.

```python
import os

def compiling():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world.jrxml'	
	jasper = pyjasper.JasperPy()
	jasper.compile(input).execute()
```

This commando will compile the `hello_world.jrxml` source file to a `hello_world.jasper` file.

####Processing

Now lets process the report that we compile before:

```python
import os

def processing():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world.jrxml'
	output = os.path.dirname(os.path.abspath(__file__)) + '/output/exemples'
	jasper = pyjasper.JasperPy()
	jasper.process(input, output, ["pdf","rtf"]).execute()
```

Now check the examples folder! :) Great right? You now have 2 files, `hello_world.pdf` and `hello_world.rtf`.

Check the *API* of the  `compile` and `process` functions in the file `pyjasper/jasperpy.py` file.

####Listing Parameters

Querying the jasper file to examine parameters available in the given jasper report file:

```python
import os

def listingParameters():
	input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world_params.jrxml'
	jasper = pyjasper.JasperPy()
	output = jasper.list_parameters(input).execute()	
	print(output)
```

###Advanced example - using a database

We can also specify parameters for connecting to database:

```python
import os
from platform import python_version
import pyjasper

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
```

**Note 2:**

For a complete list of locales see [Supported Locales](http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html)


###Reports from a XML

See how easy it is to generate a report with a source an XML file:

```python
import os

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
```

###Reports from a JSON File

See how easy it is to generate a report with a source an JSON file:

```python
import os

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
```
###Tests

All tests are in in the `pyjasper/test/report.py` 

###MySQL

We ship the [MySQL connector](http://dev.mysql.com/downloads/connector/j/) (v5.1.39) in the `pyjasper/jasperstarter/jdbc/` directory.

###PostgreSQL

We ship the [PostgreSQL](https://jdbc.postgresql.org/) (v9.4-1203) in the `pyjasper/jasperstarter/jdbc/` directory.

##Performance

Depends on the complexity, amount of data and the resources of your machine (let me know your use case).

I have a report that generates a *Invoice* with a DB connection, images and multiple pages and it takes about **3/4 seconds** to process. I suggest that you use a worker to generate the reports in the background.

##Thanks

Thanks to [Cenote GmbH](http://www.cenote.de/) for the [JasperStarter](http://jasperstarter.sourceforge.net/) tool.

##Questions?

Open a [Issue](https://github.com/jadsonbr/pyreport/issues) 

##License

MIT

##Contribute

Contribute to the community Python, feel free to contribute, make a fork!!
