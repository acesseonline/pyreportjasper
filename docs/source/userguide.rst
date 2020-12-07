##########################
PyReportJasper User Guide
##########################

.. toctree::
   :maxdepth: 2

Introduction
~~~~~~~~~~~~
This package aims to be a solution to compile and process JasperReports
(.jrxml & .jasper files).

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

No support
------------
.. warning:: For now we do not support MongoDB but we are working to make it happen


The Hello World example.
~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::

    We provide a repository with several reports that you can use to do your tests.
    Just clone your machine to open the ``run.py`` file and start coding.

    `Repository link with examples here <https://github.com/PyReportJasper/exemples_report>`__



Compiling
----------

First we need to compile our ``JRXML`` file into a ``JASPER`` binary
file. We just have to do this one time.

**Note 1:** You don't need to do this step if you are using *Jaspersoft
Studio*. You can compile directly within the program.

.. code-block:: python
   :emphasize-lines: 10

    # -*- coding: utf-8 -*-
    import os
    from pyreportjasper import PyReportJasper

    def compiling():
        REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
        input_file = os.path.join(REPORTS_DIR, 'csv.jrxml')
        output_file = os.path.join(REPORTS_DIR, 'csv')
        pyreportjasper = PyReportJasper()
        pyreportjasper.compile(write_jasper=True)

This commando will compile the ``csv.jrxml`` source file to a
``csv.jasper`` file.

Processing
----------
Now lets process the report that we compile before:

.. code-block:: python
   :emphasize-lines: 15

   # -*- coding: utf-8 -*-
   import os
   from pyreportjasper import PyReportJasper

   def processing():
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'csv.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'csv')
      pyreportjasper = PyReportJasper()
      pyreportjasper.config(
        input_file,
        output_file,
        output_formats=["pdf", "rtf"]
      )
      pyreportjasper.process_report()

Now check the reports folder! :) Great right? You now have 2 files,
``csv.pdf`` and ``csv.rtf``.


Advanced example - using a database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can also specify parameters for connecting to database:

.. code-block:: python
   :emphasize-lines: 10-19

   # -*- coding: utf-8 -*-
   import os
   from platform import python_version
   from pyreportjasper import PyReportJasper

   def advanced_example_using_database():
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'hello_world.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'hello_world')
      conn = {
        'driver': 'postgres',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'host': 'DB_HOST',
        'database': 'DB_DATABASE',
        'schema': 'DB_SCHEMA',
        'port': '5432'
        'jdbc_dir': '<path>/postgres.jar'
      }
      pyreportjasper = PyReportJasper()
      pyreportjasper.config(
        input_file,
        output_file,
        db_connection=conn,
        output_formats=["pdf", "rtf"],
        parameters={'python_version': python_version()},
        locale='en_US'
      )
      pyreportjasper.process_report()

**Note 2:**

For a complete list of locales see `Supported
Locales <http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html>`__

Reports from a XML
~~~~~~~~~~~~~~~~~~

See how easy it is to generate a report with a source an XML file:

.. code-block:: python

   # -*- coding: utf-8 -*-
   import os
   from pyreportjasper import PyReportJasper

   def xml_to_pdf():
      RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'CancelAck.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'cancel_ack2')
      data_file = os.path.join(RESOURCES_DIR, 'CancelAck.xml')
      pyreportjasper = PyReportJasper()
      self.pyreportjasper.config(
         input_file,
         output_file,
         output_formats=["pdf"],
         db_connection={
             'driver': 'xml',
             'data_file': data_file,
             'xml_xpath': '/CancelResponse/CancelResult/ID',
         }
      )
      self.pyreportjasper.process_report()
      print('Result is the file below.')
      print(output_file + '.pdf')


Reports from a CSV File
~~~~~~~~~~~~~~~~~~~~~~~~

See how easy it is to generate a report with a source an CSV file:

.. code-block:: python

   # -*- coding: utf-8 -*-
   import os
   from pyreportjasper import PyReportJasper

   def csv_to_pdf():
      RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'csv.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'csv')
      conn = {
         'driver': 'csv',
         'data_file': os.path.join(self.RESOURCES_DIR, 'csvExampleHeaders.csv'),
         'csv_charset': 'utf-8',
         'csv_out_charset': 'utf-8',
         'csv_field_del': '|',
         'csv_out_field_del': '|',
         'csv_record_del': "\r\n",
         'csv_first_row': True,
         'csv_columns': "Name,Street,City,Phone".split(",")
      }
      pyreportjasper = PyReportJasper()
      self.pyreportjasper.config(
         input_file,
         output_file,
         output_formats=["pdf"],
         db_connection=conn
      )
      self.pyreportjasper.process_report()
      print('Result is the file below.')
      print(output_file + '.pdf')


Reports from a JSON File
~~~~~~~~~~~~~~~~~~~~~~~~

See how easy it is to generate a report with a source an JSON file:

.. code-block:: python

   # -*- coding: utf-8 -*-
   import os
   from pyreportjasper import PyReportJasper

   def json_to_pdf():
      RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'json.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'json')
      conn = {
         'driver': 'json',
         'data_file': os.path.join(self.RESOURCES_DIR, 'contacts.json'),
         'json_query': 'contacts.person'
      }
      pyreportjasper = PyReportJasper()
      self.pyreportjasper.config(
         input_file,
         output_file,
         output_formats=["pdf"],
         db_connection=conn
      )
      self.pyreportjasper.process_report()
      print('Result is the file below.')
      print(output_file + '.pdf')

Reports from a JSONQL
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # -*- coding: utf-8 -*-
   import os
   from pyreportjasper import PyReportJasper

   def jsonql_to_pdf():
      RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
      REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
      input_file = os.path.join(REPORTS_DIR, 'jsonql.jrxml')
      output_file = os.path.join(REPORTS_DIR, 'jsonql')
      conn = {
         'driver': 'jsonql',
         'data_file': os.path.join(self.RESOURCES_DIR, 'contacts.json'),
         'json_query': 'contacts.person'
      }
      pyreportjasper = PyReportJasper()
      self.pyreportjasper.config(
         input_file,
         output_file,
         output_formats=["pdf"],
         db_connection=conn
      )
      self.pyreportjasper.process_report()
      print('Result is the file below.')
      print(output_file + '.pdf')
