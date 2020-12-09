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
    url='https://github.com/acesseonline/pyreportjasper',
    download_url='https://pypi.python.org/pypi/pyreportjasper/' + get_version('pyreportjasper'),
    project_urls=OrderedDict((
        ('Documentation', 'https://pyreportjasper.readthedocs.io/en/master/'),
        ('Code', 'https://github.com/acesseonline/pyreportjasper'),
        ('Issue tracker', 'https://github.com/acesseonline/pyreportjasper/issues'),
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
    platforms=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    packages=find_packages(),
    install_requires=[
        'jpype1'
    ],
    test_suite='test',
    package_data={
        'package': ['libs/*'],
    },
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
