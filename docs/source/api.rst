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


    Example:

    .. code-block:: python

        # Instantiating the class
        config = Config()
        # Defining value in a class attribute
        config.dbType = 'csv'


Class Report
~~~~~~~~~~~~~
.. py:class:: Report(config: Config, input_file)

    Class responsible for instantiating the JVM and loading the necessary Java objects for manipulating the files to compile, generate and export the reports.

    :param Config config: Config class instance
    :param str input_file: Input file (.jrxml|.jasper|.jrprint)

    .. py:classmethod:: compile()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: compile_to_file()

    description

    :return: Return description.
    :rtype: str
    .. py:classmethod:: fill()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: fill_internal()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: get_output_stream(suffix)

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_pdf()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_rtf()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_docx()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_odt()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_xml()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_xls()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_xls_meta()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_xlsx()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_csv()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_csv_meta()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_ods()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_pptx()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: export_jrprint()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: get_report_parameters()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: get_main_dataset_query()

    description

    :return: Return description.
    :rtype: str

    .. py:classmethod:: add_jar_class_path(dir_or_jar)

    description

    :return: Return description.
    :rtype: str



Class Db
~~~~~~~~~~~~~
.. py:class:: Db

    Class responsible for managing the report data source