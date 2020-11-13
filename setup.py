# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

from setuptools import setup, find_packages
import io
import os
import re
from collections import OrderedDict
import subprocess

def version_available(cmd):
    try:
        # prints version and returns 0 if successulf
        output = subprocess.call([cmd, "-version"])
        return output == 0
    except OSError as e:
        # handle file not found error.
        if e.errno == os.errno.ENOENT:
            print("error please install " + cmd)
            return False
        else:
            # Something else went wrong, raise the exception
            raise

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='pyreportjasper',
    version=get_version('pyreportjasper'),
    url='https://github.com/PyReportJasper/pyreportjasper',
    download_url='https://pypi.python.org/pypi/jpy/' + get_version('pyreportjasper'),
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/PyReportJasper/pyreportjasper/blob/master/README.rst'),
        ('Code', 'https://github.com/PyReportJasper/pyreportjasper'),
        ('Issue tracker', 'https://github.com/PyReportJasper/pyreportjasper/issues'),
    )),
    license='GPLv3',
    author='Jadson Bonfim Ribeiro',
    author_email='contato@jadsonbr.com.br',
    keywords='report jasper python',
    description='This package aims to be a solution to compile and process '
                'JasperReports (.jrxml & .jasper files).',
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    zip_safe=False,
    platforms='Windows, Linux, Darwin',
    packages=find_packages(),
    install_requires=[
        'jpy',
        'requests'
    ],
    dependency_links=[
        'https://github.com/bcdev/jpy/archive/master.zip#egg=jpy'
    ],
    test_suite='test',
    package_data={
        'package': ['jasperstarter/*'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
