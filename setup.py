# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

files = ["jasperstarter/*", "test/*"]

setup(
    name='pyreportjasper',
    version='0.1.3',
    url='https://github.com/jadsonbr/pyreport',
    license='MIT License',
    author='Jadson Bonfim Ribeiro',
    author_email='jadsonbr@outlook.com.br',
    keywords='report jasper python relatorio',
    description=u'This package aims to be a solution to compile and process '
                u'JasperReports (.jrxml & .jasper files).',
    packages=find_packages(),
    install_requires=[
    ],
    test_suite='test',
    package_data={
        'package': files,
    },
    include_package_data=True,
)
