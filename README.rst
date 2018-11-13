Reports for Python, with JasperReports.
=======================================

|Build Status| |Coverage Status| |Code Health| |PyPI|

**Is using Linux servers?**

Do not forget to grant permission 777 for the directory where is the
package.

Introduction
------------

This package aims to be a solution to compile and process JasperReports
(.jrxml & .jasper files).

Why?
~~~~

Did you ever had to create a good looking Invoice with a lot of fields
for your great web app or desktop?

I had to, and the solutions out there were not perfect. Generating
*HTML* + *CSS* to make a *PDF*? WTF? That doesn't make any sense! :)

Then I found **JasperReports** the best open source solution for
reporting.

What can I do with this?
~~~~~~~~~~~~~~~~~~~~~~~~

Well, everything. JasperReports is a powerful tool for **reporting** and
**BI**.

**From their website:**

    The JasperReports Library is the world's most popular open source
    reporting engine. It is entirely written in Java and it is able to
    use data coming from any kind of data source and produce
    pixel-perfect documents that can be viewed, printed or exported in a
    variety of document formats including HTML, PDF, Excel, OpenOffice
    and Word.

It is recommended using `Jaspersoft
Studio <http://community.jaspersoft.com/project/jaspersoft-studio>`__ to
build your reports, connect it to your datasource (ex:JSON, XML, MySQL,
POSTGRES, SQL Server), loop thru the results and output it to PDF, XLS,
DOC, RTF, ODF, etc.

*Some examples of what you can do:*

-  Invoices
-  Reports
-  Listings

Package to generate reports with
`JasperReports <http://community.jaspersoft.com/project/jasperreports-library>`__
library through
`JasperStarter <https://bitbucket.org/cenote/jasperstarter/src>`__
command-line tool.

Requirements
------------

-  Java JDK 1.8
-  Python
   `subprocess.run() <https://docs.python.org/3/library/subprocess.html>`__
   function

Optional
--------

-  `Mysql JDBC <http://dev.mysql.com/downloads/connector/j/>`__ (if you
   want to use database)
-  `PostgreSQL JDBC <https://jdbc.postgresql.org/download.html>`__ (if
   you want to use database)
-  `SQL Server
   JDBC <https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=11774>`__
   (if you want to use database)
-  `Oracle
   JDBC <http://www.oracle.com/technetwork/apps-tech/jdbc-112010-090769.html>`__
   (if you want to use database)
-  `MongoDB JDBC <https://mongodb.github.io/mongo-java-driver/>`__ (if
   you want to use database)
-  `Jaspersoft
   Studio <http://community.jaspersoft.com/project/jaspersoft-studio>`__
   (to draw and compile your reports)

Note
~~~~

-  The JDBC driver of your database should be place in the
   ``pyreportjasper/jasperstarter/jdbc/`` directory.
-  Using **pyreportjasper**, you can also access different types of data
   sources, including CSV, JDBC, JSON, NoSQL, XML, or your own custom
   data source.

Java (JDK and JRE)
~~~~~~~~~~~~~~~~~~

Check if you already have Java installed:

::

    $ javac -version
    javac version 1.8.0_101

If you get:

::

    command not found: javac

Then install it with: (Ubuntu/Debian)

::

    $ sudo apt-get install default-jdk

To install on: (centOS/Fedora)

::

    # yum install java-1.8.0-openjdk.x86_64

To install on windows visit the link->
`JDK <http://www.oracle.com/technetwork/pt/java/javase/downloads/jdk8-downloads-2133151.html>`__
and look for the most appropriate version for your system.

Now run the ``javac -version`` again and check if the output is ok.

Installation
------------

Install `PyPI <https://pypi.python.org/pypi/pyreportjasper>`__ if you
don't have it.

::

    pip install pyreportjasper

Using the code
~~~~~~~~~~~~~~~

Pyreport is actively developed in GitHub, where code is `always
available <https://github.com/jadsonbr/pyreportjasper>`__.

You can clone the public repository:

::

    git clone git://github.com/jadsonbr/pyreportjasper.git

Download `tar
file <https://github.com/jadsonbr/pyreportjasper/tarball/master>`__:

::

    curl -OL https://github.com/jadsonbr/pyreportjasper/tarball/master

Or, Download the `zip
file <https://github.com/jadsonbr/pyreportjasper/zipball/master>`__:

::

    curl -OL https://github.com/jadsonbr/pyreportjasper/zipball/master

Unzip the downloaded file

Navigate to the unzipped folder

Once you have a copy of the code, you can easily include it in your
Pytohn package, or install it in your site-packages directory:

::

    $ python setup.py install

Examples
--------

The *Hello World* example.
~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to the examples directory in the root of the package Open the
``test/examples/hello_world.jrxml`` file with Jaspersoft Studio or with
your favorite text editor and take a look at the source code.

Compiling
^^^^^^^^^

First we need to compile our ``JRXML`` file into a ``JASPER`` binary
file. We just have to do this one time.

**Note 1:** You don't need to do this step if you are using *Jaspersoft
Studio*. You can compile directly within the program.

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def compiling():
        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/hello_world.jrxml'
        jasper = JasperPy()
        jasper.compile(input_file)

This commando will compile the ``hello_world.jrxml`` source file to a
``hello_world.jasper`` file.

Processing
^^^^^^^^^^

Now lets process the report that we compile before:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def processing():
        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/hello_world.jrxml'
        output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
        jasper = JasperPy()
        jasper.process(
            input_file, output_file=output, format_list=["pdf", "rtf"])

Now check the examples folder! :) Great right? You now have 2 files,
``hello_world.pdf`` and ``hello_world.rtf``.

Check the *API* of the ``compile`` and ``process`` functions in the file
``pyreportjasper/jasperpy.py`` file.

Listing Parameters
^^^^^^^^^^^^^^^^^^

Querying the jasper file to examine parameters available in the given
jasper report file:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def listing_parameters():
        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/hello_world_params.jrxml'
        jasper = JasperPy()
        output = jasper.list_parameters(input_file)
        print(output)

Advanced example - using a database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can also specify parameters for connecting to database:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from platform import python_version
    from pyreportjasper import JasperPy

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
        jasper = JasperPy()
        jasper.process(
            input_file,
            output_file=output,
            format_list=["pdf", "rtf", "xml"],
            parameters={'python_version': python_version()},
            db_connection=con,
            locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
        )

**Note 2:**

For a complete list of locales see `Supported
Locales <http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html>`__

Reports from a XML
~~~~~~~~~~~~~~~~~~

See how easy it is to generate a report with a source an XML file:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def xml_to_pdf():
        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/CancelAck.jrxml'

        output = os.path.dirname(os.path.abspath(__file__)) + '/output/_CancelAck'

        data_file = os.path.dirname(os.path.abspath(__file__)) + \
            '/examples/CancelAck.xml'

        jasper = JasperPy()

        jasper.process(
            input_file,
            output_file=output,
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
        

Reports from a JSON File
~~~~~~~~~~~~~~~~~~~~~~~~

See how easy it is to generate a report with a source an JSON file:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def json_to_pdf():
        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/json.jrxml'

        output = os.path.dirname(os.path.abspath(__file__)) + '/output/_Contacts'
        json_query = 'contacts.person'

        data_file = os.path.dirname(os.path.abspath(__file__)) + \
            '/examples/contacts.json'

        jasper = JasperPy()
        jasper.process(
            input_file,
            output_file=output,
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

Subreport Example
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy

    def subreport_example():

        input_file_header = os.path.dirname(os.path.abspath(__file__)) + \
                            '/examples/subreports/header.jrxml'

        input_file_details = os.path.dirname(os.path.abspath(__file__)) + \
                             '/examples/subreports/details.jrxml'

        input_file_main = os.path.dirname(os.path.abspath(__file__)) + \
                          '/examples/subreports/main.jrxml'

        input_file = os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/subreports/main.jasper'

        data_file = os.path.dirname(os.path.abspath(__file__)) + \
                    '/examples/subreports/contacts.xml'

        output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples/subreports/'

        jasper = JasperPy()

        jasper.compile(input_file_header)
        jasper.compile(input_file_details)
        jasper.compile(input_file_main)

        jasper.process(
                    input_file,
                    output_file=output,
                    format_list=["pdf"],
                    parameters={},
                    db_connection={
                        'data_file': data_file,
                        'driver': 'xml',
                        'xml_xpath': '"/"',
                    },
                    locale='pt_BR',  # LOCALE Ex.:(en_US, de_GE)
                    resource='examples/subreports/'
                )

Flask Example
~~~~~~~~~~~~~

Get parameters via URL and filter them if they are valid parameters for
the *jrxml* file:

After runnig you could visit
http://localhost:5000/?myString=My%20Beautiful%20String&myInt=1&myDate=2017-01-01&this\_parameter=ignored

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import JasperPy
    from flask import Flask, request, make_response


    app = Flask(__name__)
    input_file =  os.path.dirname(os.path.abspath(__file__)) + \
                     '/examples/hello_world_params.jrxml'
    jasper = JasperPy()


    def compiling():
        jasper.compile(input_file)

    def processing(parameters):
        output_file = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
        jasper.process(
            input_file, output_file, parameters=parameters, format_list=["pdf"])

    def filter_parameters(request_args):
        list_parameters = jasper.list_parameters(input_file)
        parameters = {}
        for key in list_parameters:
          if key in request_args:
            parameters[key] = request_args[key]
        return parameters

    @app.route('/')
    def my_route():
      request_args = request.args.to_dict()
      parameters = filter_parameters(request_args)

      processing(parameters)

      try:
          with app.open_resource(os.path.dirname(os.path.abspath(__file__)) + '/output/examples/hello_world_params.pdf') as f:
              content = f.read()
          resposta = make_response(content)
          resposta.headers['Content-Type'] = 'application/pdf; charset=utf-8'
          resposta.headers['Content-Disposition'] = 'inline; filename=hello_world_params.pdf'
          return resposta
      except IOError:
          return make_response("<h1>403 Forbidden</h1>", 403)

    if __name__ == '__main__':
        compiling()
        app.run(host='0.0.0.0')

Working with resources (i18n resource bundles, icons or images)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need provide resource to report, you can do that by set parameter
``resource`` in method ``jasper.process``. More details `jasper starter
manual
page <http://jasperstarter.cenote.de/usage.html#Reports_with_resources>`__.

.. code-block:: python

    # -*- coding: utf-8 -*-
    import os
    from platform import python_version
    from pyreportjasper import JasperPy

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
        jasper = JasperPy()
        jasper.process(
            input_file,
            output_file=output,
            format_list=["pdf", "rtf", "xml"],
            parameters={'python_version': python_version()},
            db_connection=con,
            locale='pt_BR',  # LOCALE Ex.:(en_US, de_GE)
            resource='path/to/my/resource/myresource.jar'
        )

Tests
~~~~~

All tests are in in the ``test`` directory. To run them

::

    python setup.py test

Performance
-----------

Depends on the complexity, amount of data and the resources of your
machine (let me know your use case).

I have a report that generates a *Invoice* with a DB connection, images
and multiple pages and it takes about **3/4 seconds** to process. I
suggest that you use a worker to generate the reports in the background.

Questions?
----------

Open a `Issue <https://github.com/jadsonbr/pyreportjasper/issues>`__

Contribute
----------

Contribute to the community Python, feel free to contribute, make a
fork!!

Contributors
~~~~~~~~~~~~

-  `List of
   contributors <https://github.com/jadsonbr/pyreportjasper/graphs/contributors>`__

Thanks
------

Thanks to `Cenote GmbH <http://www.cenote.de/>`__ for the
`JasperStarter <http://jasperstarter.sourceforge.net/>`__ tool.

.. |Build Status| image:: https://travis-ci.org/jadsonbr/pyreportjasper.svg?branch=master
   :target: https://travis-ci.org/jadsonbr/pyreportjasper
.. |Coverage Status| image:: https://coveralls.io/repos/github/jadsonbr/pyreportjasper/badge.svg?branch=master
   :target: https://coveralls.io/github/jadsonbr/pyreportjasper?branch=master
.. |Code Health| image:: https://landscape.io/github/jadsonbr/pyreportjasper/master/landscape.svg?style=flat
   :target: https://landscape.io/github/jadsonbr/pyreportjasper/master
.. |PyPI| image:: https://img.shields.io/pypi/l/pyreportjasper.svg
   :target: https://github.com/jadsonbr/pyreportjasper/blob/master/LICENSE
