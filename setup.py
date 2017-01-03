# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2017 Jadson Bonfim Ribeiro <jadsonbr@outlook.com.br>
#

from setuptools import setup, find_packages
import os
import re


def get_version(package):
    """
    Based in https://github.com/tomchristie/django-rest-framework/blob/
    971578ca345c3d3bae7fd93b87c41d43483b6f05/setup.py
    :param package Package name
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    name='pyreportjasper',
    version=get_version('pyjasper'),
    url='https://github.com/jadsonbr/pyreport',
    license='MIT License',
    author='Jadson Bonfim Ribeiro',
    author_email='jadsonbr@outlook.com.br',
    keywords='report jasper python',
    description='This package aims to be a solution to compile and process '
                'JasperReports (.jrxml & .jasper files).',
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
        'Programming Language :: Python :: 2.7 3.3 3.4 3.5',
    ],
)
