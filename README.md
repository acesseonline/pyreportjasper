# Reports for Python, with JasperReports.
[![Build Status](https://travis-ci.org/multidadosti-erp/pyreport.svg?branch=feature%2Fpyjasper_adjust)](https://travis-ci.org/multidadosti-erp/pyreport)
[![Coverage Status](https://coveralls.io/repos/github/multidadosti-erp/pyreport/badge.svg?branch=feature%2Fpyjasper_adjust)](https://coveralls.io/github/multidadosti-erp/pyreport?branch=feature%2Fpyjasper_adjust)
[![Code Health](https://landscape.io/github/multidadosti-erp/pyreport/feature/pyjasper_adjust/landscape.svg?style=flat)](https://landscape.io/github/multidadosti-erp/pyreport/feature/pyjasper_adjust)
[![PyPI](https://img.shields.io/pypi/l/pyreportjasper.svg)](https://github.com/multidadosti-erp/pyreport/blob/master/LICENSE)

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

Install [PyPI](https://pypi.python.org/pypi/pyreportjasper) if you don't have it.
```
pip install pyreportjasper
```

and that's it.

##Examples

###The *Hello World* example.

Go to the examples directory in the root of the package 
Open the `test/examples/hello_world.jrxml` file with Jaspersoft Studio or with your favorite text editor and take a look at the source code.

#### Compiling

First we need to compile our `JRXML` file into a `JASPER` binary file. We just have to do this one time.

**Note 1:** You don't need to do this step if you are using *Jaspersoft Studio*. You can compile directly within the program.

```python
import os
import pyjasper

def compiling():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    jasper = pyjasper.JasperPy()
    jasper.compile(input_file)

```

This commando will compile the `hello_world.jrxml` source file to a `hello_world.jasper` file.

####Processing

Now lets process the report that we compile before:

```python
import os
import pyjasper

def processing():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file, output=output, format_list=["pdf", "rtf"])

```

Now check the examples folder! :) Great right? You now have 2 files, `hello_world.pdf` and `hello_world.rtf`.

Check the *API* of the  `compile` and `process` functions in the file `pyjasper/jasperpy.py` file.

####Listing Parameters

Querying the jasper file to examine parameters available in the given jasper report file:

```python
import os
import pyjasper

def listing_parameters():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world_params.jrxml'
    jasper = pyjasper.JasperPy()
    output = jasper.list_parameters(input_file)
    print(output)

```

###Advanced example - using a database

We can also specify parameters for connecting to database:

```python
import os
from platform import python_version
import pyjasper

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
    )

```

**Note 2:**

For a complete list of locales see [Supported Locales](http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html)


###Reports from a XML

See how easy it is to generate a report with a source an XML file:

```python
import os
import pyjasper

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
    )

    print('Result is the file below.')
    print(output + '.pdf')
    
```

###Reports from a JSON File

See how easy it is to generate a report with a source an JSON file:

```python
import os
import pyjasper

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
    )

    print('Result is the file below.')
    print(output + '.pdf')
```

###Tests

All tests are in in the `test` directory. To run them

```
python setup.py test
```

###MySQL

We ship the [MySQL connector](http://dev.mysql.com/downloads/connector/j/) (v5.1.39) in the `pyjasper/jasperstarter/jdbc/` directory.

###PostgreSQL

We ship the [PostgreSQL](https://jdbc.postgresql.org/) (v9.4-1203) in the `pyjasper/jasperstarter/jdbc/` directory.

###MSSQL

[Microsoft JDBC Drivers 6.0, 4.2, 4.1, and 4.0 for SQL Server
](https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=11774).

##Performance

Depends on the complexity, amount of data and the resources of your machine (let me know your use case).

I have a report that generates a *Invoice* with a DB connection, images and multiple pages and it takes about **3/4 seconds** to process. I suggest that you use a worker to generate the reports in the background.

##Questions?

Open a [Issue](https://github.com/jadsonbr/pyreport/issues) 

##Contribute

Contribute to the community Python, feel free to contribute, make a fork!!

### Contributors

* Michell Stuttgart <michellstut@gmail.com>

##Thanks

Thanks to [Cenote GmbH](http://www.cenote.de/) for the [JasperStarter](http://jasperstarter.sourceforge.net/) tool.
