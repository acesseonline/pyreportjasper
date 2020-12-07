# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath(__file__ + "/../../../"))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PyReportJasper'
copyright = '2020, Jadson Bonfim Ribeiro'
author = 'Jadson Bonfim Ribeiro'

# The full version, including alpha/beta/rc tags
import pyreportjasper
release = pyreportjasper.__version__
version = pyreportjasper.__version__

man_pages = [
    ('index', 'PyReportJasper', 'PyReportJasper Documentation',
     ['PyReportJasper Project'], 1)
]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'readthedocs_ext.readthedocs'
]
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# import guzzle_sphinx_theme
# extensions.append("guzzle_sphinx_theme")
# html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'
# html_show_sourcelink = False
# html_sidebars = {
#     '**': ['logo-text.html',
#            'globaltoc.html',
#            'searchbox.html']
# }

html_logo = 'logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
    ],
}

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
html_theme = 'default'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


napoleon_custom_sections = ["Static Methods", "Virtual Methods", "Constructors"]