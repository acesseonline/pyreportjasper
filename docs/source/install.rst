Installation
============

PyReportJasper is available either as a pre-compiled binary for Anaconda and PYPI, or may be
built from source though various methods.

Binary Install
--------------

PyReportJasper can be installed as pre-compiled binary if you are using the `Anaconda
<https://anaconda.org>`_ Python stack. Binaries are available for Linux, OSX,
and windows on conda-forge.

1. Ensure you have installed Anaconda/Miniconda. Instructions can be found
   `here <http://conda.pydata.org/docs/install/quick.html>`__.
2. Install from
   the conda-forge software channel::

    conda install -c conda-forge pyreportjasper

3. Or install from the acesseonline software channel::

    conda install -c acesseonline pyreportjasper

Source Install
--------------

Installing from source requires:

Python
  PyReportJasper works CPython 3.5 or later. Both the runtime and the development
  package are required.

Java
  Either the Sun/Oracle JDK/JRE Variant or OpenJDK.
  PyReportJasper has been tested with Java versions from Java 1.9 to Java 15.

Jpype1
  JPype is a Python module to provide full access to Java from within Python.


Once these requirements have been met, one can use pip to build from either the
source distribution or directly from the repository.  Specific requirements from
different achitectures are listed below.

Build using pip
~~~~~~~~~~~~~~~

PyReportJasper may be built and installed with one step using pip.

To install the latest PyReportJasper, use: ::

  pip install pyreportjasper

This will install PyReportJasper either from source or binary distribution, depending on
your operating system and pip version.

To install from the current github master use: ::

  pip install git@github.com:acesseonline/pyreportjasper.git

More details on installing from git can be found at `Pip install
<https://pip.pypa.io/en/stable/reference/pip_install/#git>`__.  The git version
does not include a prebuilt jar the JDK is required.


Build and install manually
~~~~~~~~~~~~~~~~~~~~~~~~~~

PyReportJasper can be built entirely from source.

**1. Get the PyReportJasper source**

The PyReportJasper source may be acquired from either
`github <https://github.com/acesseonline/pyreportjasper>`__ or
from `PyPi <https://pypi.org/project/pyreportjasper/>`__.

**2. Build the source with desired options**

Compile PyReportJasper using the included ``setup.py`` script: ::

  python setup.py build

**3. Test PyReportJasper with (optional):** ::

    python -m unittest discover ./test -p '*.py'

**4. Install PyReportJasper with:** ::

    python setup.py install

If it fails...
~~~~~~~~~~~~~~

Most failures happen when setup.py is unable to find the JDK home directory
which shouble be set in the enviroment variable ``JAVA_HOME``.  If this
happens, preform the following steps:

1. Identify the location of your JDK systems installation and set the environment variable. ::

     export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

2. If that setup.py still fails please create an Issue `on
   github <https://github.com/acesseonline/pyreportjasper/issues?state=open>`__ and
   post the relevant logs.

.. _below:

Platform Specific requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyReportJasper is known to work on Linux, OSX, and Windows.  To make it easier to those
who have not built CPython modules before here are some helpful tips for
different machines.

Debian/Ubuntu
:::::::::::::

Debian/Ubuntu users will have to install ``g++`` and ``python-dev``.
Use:

    sudo apt-get install g++ python-dev python3-dev

Windows
:::::::

CPython modules must be built with the same C++ compiler used to build Python.
The tools listed below work for Python 3.5 to 3.9.  Check with `Python dev guide
<https://devguide.python.org/setup/>`_ for the latest instructions.

1. Install your desired version of Python (3.5 or higher), e.g., `Miniconda
   <https://docs.conda.io/en/latest/miniconda.html#windows-installers>`_ is a good choice for users not yet
   familiar with the language
2. For Python 3 series, Install either 2017 or 2019 Visual Studio.
   `Microsoft Visual Studio 2019 Community Edition
   <https://visualstudio.microsoft.com/downloads/>`_ is known to work.

From the Python developer page:

   When installing Visual Studio 2019, select the Python development workload and
   the optional Python native development tools component to obtain all of the
   necessary build tools. If you do not already have git installed, you can find
   git for Windows on the Individual components tab of the installer.

When building for windows you must use the Visual Studio developer command
prompt.