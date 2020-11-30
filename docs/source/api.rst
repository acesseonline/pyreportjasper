API Reference
=============

Class Config
~~~~~~~~~~~~~

.. py:class:: Config(*args, **kwargs)

    Class for defining the settings to generate the reports.

    .. py:attribute:: jvm_maxmem

        Maximum memory used by the JVM

    :type: str
    :value: '512M'

    .. py:attribute:: jvm_classpath

        The class path is the path that the Java runtime environment searches for classes and other resource files.

    :type: str

    .. py:attribute:: dbType

        Data source type

    :type: str
    :options: ``None``, ``csv``, ``xml``, ``json``, ``jsonql``, ``mysql``, ``postgres``, ``oracle``, ``generic``

    .. py:attribute:: dbDriver

        Jdbc driver class name for use with dbType: generic

    :type: str

    .. py:attribute:: dbHost

        Database host

    :type: str

    .. py:attribute:: dbName

        Database name

    :type: str

    .. py:attribute:: dbPasswd

        Database password

    :type: str

    .. py:attribute:: dbPort

        Database port

    :type: int

    .. py:attribute:: dbSid

        Oracle sid

    :type: str

    .. py:attribute:: dbUrl

        Jdbc url without user, passwd with dbType: generic

    :type: str

    .. py:attribute:: dbUser

        Database user

    :type: str

    .. py:attribute:: jdbcDir

        Directory where  jdbc  driver  jars  are  located.

    :type: str

    .. py:attribute:: input

        Input file (.jrxml|.jasper|.jrprint)

    :type: str

    .. py:attribute:: dataFile

        Input file for file based  datasource

    :type: str

    .. py:attribute:: csvFirstRow

        First row contains column headers

    :type: bool

    .. py:attribute:: csvColumns

        Comma separated list of column names

    :type: list(str)

    .. py:attribute:: csvRecordDel

        CSV Record Delimiter - defaults to line.separator

    :type: str

    .. py:attribute:: csvFieldDel

        CSV Field Delimiter - defaults to ","

    :type: str

    .. py:attribute:: csvCharset

        CSV charset - defaults to "utf-8"

    :type: str

    .. py:attribute:: xmlXpath

        XPath for XML Datasource

    :type: str

    .. py:attribute:: jsonQuery

        JSON query string for JSON Datasource

    :type: str

    .. py:attribute:: jsonQLQuery

        JSONQL query string for JSONQL Datasource

    :type: str

    .. py:attribute:: locale

        Set locale with two-letter ISO-639 code or a combination of ISO-639 and ISO-3166 like en_US.

        For a complete list of locales see `Supported Locales <http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html>`__

    :type: str

    .. py:attribute:: output

        Directory or basename of outputfile(s)

    :type: str

    .. py:attribute:: outputFormats

        A list of output formats

    :type: list(str)
    :options:  ``pdf``, ``rtf``, ``docx``, ``odt``, ``xml``, ``xls``, ``xlsx``, ``csv``, ``csv_meta``, ``ods``, ``pptx``, ``jrprint``

    .. py:attribute:: params

        Dictionary with the names of the parameters and their respective values.

        Exemple: ``{'NAME_PARAM_1': 'value param 1', 'NAME_PARAM_2': 'value param 2'}``

    :type: dict

    .. py:attribute:: printerName

        Name of printer

    :type: str

    .. py:attribute:: reportName

        Set internal report/document name when printing

    :type: str

    .. py:attribute:: resource

        Path to  report  resource  dir  or  jar  file.  If <resource> is not  given  the  input  directory is used.

    :type: str

    .. py:attribute:: writeJasper

        Write .jasper  file  to  imput  dir  if  jrxml  is processed

    :type: bool
    :value: False

    .. py:attribute:: outFieldDel

        Export CSV (Metadata)  Field  Delimiter - defaults to ","

    :type: str

    .. py:attribute:: outCharset

        Export CSV (Metadata) Charset  - defaults to "utf-8"

    :type: str

    .. py:attribute:: askFilter

    :type: str
    :options:
        ``a`` - all (user and system definded) prarms

        ``ae`` - all empty params

        ``u`` - user params

        ``ue`` - empty user params

        ``p`` - user params marked for prompting

        ``pe`` - empty user params markted for prompting

    .. py:classmethod:: has_output()

    Valid if there is a path or file for the output

    :return: Returns true if there is a defined path or file for output otherwise false.
    :rtype: bool

    .. py:classmethod:: is_write_jasper()

    Valid if it is to generate a .jasper

    :return: Returns ``true`` if the .jasper is to be generated, otherwise it is ``false``.
    :rtype: bool

    .. py:classmethod:: has_jdbc_dir()

    Validates if there is a path or file for jdbc .jar

    :return: Returns ``true`` if it exists, otherwise ``false``.
    :rtype: bool

    .. py:classmethod:: has_resource()

    Validates if there is a .jar or path with several .jar to add to the class path

    :return: Returns ``true`` if it exists, otherwise ``false``.
    :rtype: bool


Class Report
~~~~~~~~~~~~~
.. py:class:: Report(config: Config, input_file)

    Class responsible for instantiating the JVM and loading the necessary Java objects for manipulating the files to compile, generate and export the reports.

    :param Config config: Config class instance
    :param str input_file: Input file (.jrxml|.jasper|.jrprint)

    .. py:classmethod:: compile()

        Compile the report

    .. py:classmethod:: compile_to_file()

        Emit a .jasper compiled version of the report definition .jrxml file.

    .. py:classmethod:: fill()

        Executes the ``fill_internal()`` method

    .. py:classmethod:: fill_internal()

        Method responsible for filling the report

    .. py:classmethod:: get_output_stream(suffix)

        Return a file-based output stream with the given suffix

        :param str suffix: File suffix

        :return: Returns an output stream from the input file.
        :rtype: OutputStream (java)

    .. py:classmethod:: export_pdf()

        Export the report in ``pdf`` format

    .. py:classmethod:: export_rtf()

        Export the report in ``rtf`` format

    .. py:classmethod:: export_docx()

        Export the report in ``docx`` format

    .. py:classmethod:: export_odt()

        Export the report in ``odt`` format

    .. py:classmethod:: export_xml()

        Export the report in ``xml`` format

    .. py:classmethod:: export_xls()

        Export the report in ``xls`` format

    .. py:classmethod:: export_xls_meta()

        Export the report in ``xls`` Metadata Exporter format

    .. py:classmethod:: export_xlsx()

        Export the report in ``xlsx`` format

    .. py:classmethod:: export_csv()

        Export the report in ``csv`` format

    .. py:classmethod:: export_csv_meta()

        Export the report in ``csv`` Metadata Exporter format

    .. py:classmethod:: export_ods()

        Export the report in ``ods`` format

    .. py:classmethod:: export_pptx()

        Export the report in ``pptx`` format

    .. py:classmethod:: export_jrprint()

        Export the report in ``jrprint`` format

    .. py:classmethod:: get_report_parameters()

        Returns a list of all report parameters

        :return: Returns a list of parameters
        :rtype: list(str)

    .. py:classmethod:: get_main_dataset_query()

        For JSON, JSONQL and any other data types that need a query to be provided, an obvious default is to use the one written into the report, since that is likely what the report designer debugged/intended to be used. This provides access to the value so it can be used as needed.

        :return: Return a string of main dataset query.
        :rtype: str

    .. py:classmethod:: add_jar_class_path(dir_or_jar)

        Method responsible for adding a ``.jar`` to ``class_path`` or a list of ``.jar`` files in an informed directory

        :param str dir_or_jar: A ``.jar`` file or directory containing one or more ``.jar``



Class Db
~~~~~~~~~~~~~
.. py:class:: Db

    Class responsible for managing the report data source

    .. py:classmethod:: get_csv_datasource(config: Config)

        Method responsible for creating a data source from an informed csv file

        :param Config config: Config class instance
        :return: Returns a data source of type csv
        :rtype: ``net.sf.jasperreports.engine.data.JRCsvDataSource`` (java)

    .. py:classmethod:: get_xml_datasource(config: Config)

        Method responsible for creating a data source from an informed xml file

        :param Config config: Config class instance
        :return: Returns a data source of type xml
        :rtype: ``net.sf.jasperreports.engine.data.JRXmlDataSource`` (java)

    .. py:classmethod:: get_json_datasource(config: Config)

        Method responsible for creating a data source from an informed json file

        :param Config config: Config class instance
        :return: Returns a data source of type json
        :rtype: ``net.sf.jasperreports.engine.data.JsonDataSource`` (java)

    .. py:classmethod:: get_jsonql_datasource(config: Config)

        Method responsible for creating a data source from an informed json file

        :param Config config: Config class instance
        :return: Returns a data source of type jsonql
        :rtype: ``net.sf.jasperreports.engine.data.JsonQLDataSource`` (java)

    .. py:classmethod:: get_data_file_input_stream(config: Config)

        Get InputStream corresponding to the configured dataFile.

        :param Config config: Config class instance
        :return: Returns a InputStream
        :rtype: ``java.io.InputStream`` (java)

    .. py:classmethod:: get_connection(config: Config)

        Method responsible for obtaining a connection to a database

        :return: Returns database connection
        :rtype: ``java.sql.Connection`` (java)

