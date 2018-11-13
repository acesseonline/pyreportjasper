# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2017 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

from setuptools import setup, find_packages
import io
import os
import re
from collections import OrderedDict


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    name='pyreportjasper',
    version=get_version('pyreportjasper'),
    url='https://github.com/jadsonbr/pyreportjasper',
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/jadsonbr/pyreportjasper/blob/master/README.rst'),
        ('Code', 'https://github.com/jadsonbr/pyreportjasper'),
        ('Issue tracker', 'https://github.com/jadsonbr/pyreportjasper/issues'),
    )),
    license='MIT License',
    author='Jadson Bonfim Ribeiro',
    author_email='contato@jadsonbr.com.br',
    keywords='report jasper python',
    description='This package aims to be a solution to compile and process '
                'JasperReports (.jrxml & .jasper files).',
    long_description=readme,
    zip_safe=False,
    platforms='any',
    packages=find_packages(),
    install_requires=[
    ],
    test_suite='test',
    package_data={
        'package': ['jasperstarter/*'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
