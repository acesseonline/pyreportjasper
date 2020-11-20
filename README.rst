Reports for Python, with JasperReports.
=======================================

|License| |Donate| |PythonVersion| |Java| |Test|

New version 2.1.0 in developing
-------------------------------
Things have changed, wait

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

Requirements
------------

-  Java JDK 9+
-  Python >=3.5
-  Lib `jpype1 <https://pypi.org/project/JPype1/>`__

No support
------------
.. image:: docs/mongodb-not-supported.jpg

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
-  `Jaspersoft
   Studio <http://community.jaspersoft.com/project/jaspersoft-studio>`__
   (to draw and compile your reports)

Note
~~~~

-  Using **pyreportjasper**, you can also access different types of data
   sources, including CSV, JDBC, JSON, NoSQL, XML, or your own custom
   data source.

Tests
~~~~~

All tests are in in the ``test`` directory. To run them

::

    python setup.py test

Or with Docker

::

    docker build -f docker_files/python3_8_6-java11.Dockerfile -t pyreportjasper-python38-java11 . && docker run --name pyreportjasper-python38-java11 pyreportjasper-python38-java11

Performance
-----------

Depends on the complexity, amount of data and the resources of your
machine (let me know your use case).

I have a report that generates a *Invoice* with a DB connection, images
and multiple pages and it takes about **3/4 seconds** to process. I
suggest that you use a worker to generate the reports in the background.

Questions?
----------

Open a `Issue <https://github.com/PyReportJasper/pyreportjasper/issues>`__

Contribute
----------

Contribute to the community Python, feel free to contribute, make a
fork!!

Contributors
~~~~~~~~~~~~

-  `List of
   contributors <https://github.com/PyReportJasper/pyreportjasper/graphs/contributors>`__


.. |License| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://github.com/PyReportJasper/pyreportjasper/blob/master/LICENSE
.. |Donate| image:: https://img.shields.io/badge/donate-help%20keep-EB4A3B.svg
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=V2SUB9RQHYUGE&lc=US&item_name=pyreportjasper&item_number=pyreportjasper&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted
.. |PythonVersion| image:: https://img.shields.io/badge/python-%3E=3.0-blue
   :target: https://pypi.org/project/pyreportjasper/
.. |Java| image:: https://img.shields.io/badge/java-%3E=9-purple.svg
.. |Test| image:: https://github.com/PyReportJasper/pyreportjasper/workflows/PyReportJasper%20Tests/badge.svg?branch=development