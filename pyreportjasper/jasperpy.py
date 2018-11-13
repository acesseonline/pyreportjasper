# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2017 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
import subprocess
import logging
import re
import xml.etree.ElementTree as ET

FORMATS = (
    'pdf',
    'rtf',
    'xls',
    'xlsx',
    'docx',
    'odt',
    'ods',
    'pptx',
    'csv',
    'html',
    'xhtml',
    'xml',
    'jrprint',
)

EXECUTABLE = 'jasperstarter'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JasperPy:

    def __init__(self, resource_dir=False):

        self.path_executable = os.path.dirname(os.path.abspath(__file__)) \
                               + '/jasperstarter/bin'

        self.windows = True if os.name == 'nt' else False
        self._command = ''

        if not resource_dir:
            resource_dir = os.path.dirname(os.path.abspath(__file__)) \
                           + '/jasperstarter/bin'
        else:
            if not os.path.exists(resource_dir):
                raise NameError('Invalid resource directory!')

        # Path to report resource dir or jar file
        self.resource_directory = resource_dir

    def compile(self, input_file, output_file=False):

        if not input_file:
            raise NameError('No input file!')

        command = self.path_executable + '/' + EXECUTABLE

        command += ' compile '
        command += "\"%s\"" % input_file

        if output_file:
            command += ' -o ' + "\"%s\"" % output_file

        self._command = command

        return self.execute()

    def process(self, input_file, output_file=False, format_list=['pdf'],
                parameters={}, db_connection={}, locale='pt_BR', resource=""):

        if not input_file:
            raise NameError('No input file!')

        if isinstance(format_list, list):
            if any([key not in FORMATS for key in format_list]):
                raise NameError('Invalid format!')
        else:
            raise NameError("'format_list' value is not list!")

        command = self.path_executable + '/' + EXECUTABLE

        command += " --locale %s" % locale
        command += ' process '
        command += "\"%s\"" % input_file

        if output_file:
            command += ' -o ' + "\"%s\"" % output_file

        command += ' -f ' + ' '.join(format_list)

        if len(parameters) > 0:
            command += ' -P '
            for key, value in parameters.items():
                param = key + '="' + value + '" '
                command += " " + param + " "

        if len(db_connection) > 0:
            command += ' -t ' + db_connection['driver']

            if 'username' in db_connection:
                command += " -u " + db_connection['username']

            if 'password' in db_connection:
                command += ' -p ' + db_connection['password']

            if 'host' in db_connection:
                command += ' -H ' + db_connection['host']

            if 'database' in db_connection:
                command += ' -n ' + db_connection['database']

            if 'port' in db_connection:
                command += ' --db-port ' + db_connection['port']

            if 'jdbc_driver' in db_connection:
                command += ' --db-driver ' + db_connection['jdbc_driver']

            if 'jdbc_url' in db_connection:
                command += ' --db-url ' + db_connection['jdbc_url']

            if 'jdbc_dir' in db_connection:
                command += ' --jdbc-dir ' + db_connection['jdbc_dir']

            if 'db_sid' in db_connection:
                command += ' --db-sid ' + db_connection['db_sid']

            if 'xml_xpath' in db_connection:
                command += ' --xml-xpath ' + db_connection['xml_xpath']

            if 'data_file' in db_connection:
                command += ' --data-file ' + db_connection['data_file']

            if 'json_query' in db_connection:
                command += ' --json-query ' + db_connection['json_query']

            if 'jsonql_query' in db_connection:
                command += ' --jsonql-query ' + db_connection['jsonql_query']

        if resource != "":
            if (resource == "."):
                command += " -r "
            else:
                command += " -r " + resource

        self._command = command

        return self.execute()

    @staticmethod
    def list_parameters(input_xml):

        if not input_xml:
            raise NameError('No input file!')

        f = open(input_xml, 'r')
        f_content = f.read()
        f.close()
        xmlstring = re.sub(' xmlns="[^"]+"', '', f_content, count=1)

        param_dic = {}
        tree = ET.fromstring(xmlstring)
        for item in tree.findall(
                'parameter'):
            if item.get('name'):
                param_dic.update({item.get('name'): [item.get('class')]})
            if list(item):
                param_dic[item.get('name')].append(list(item)[0].text)
            else:
                param_dic[item.get('name')].append('')
        return param_dic

    @property
    def command(self):
        return self._command

    def execute(self, run_as_user=False):
        if run_as_user and (not self.windows):
            self._command = 'su -u ' + run_as_user + " -c \"" + \
                               self.command + "\""

        if os.path.isdir(self.path_executable):
            try:
                output = subprocess.run(
                    self.command, shell=True, check=True).returncode
            except AttributeError:
                output = subprocess.check_call(self.command, shell=True)
            except subprocess.CalledProcessError as e:
                logger.exception(str(e))
                raise NameError('Your report has an error and couldn '
                                r'\'t be processed!\ Try to output the '
                                'command using the attribute `command;` '
                                'and run it manually in the console!')
        else:
            raise NameError('Invalid resource directory!')

        return output
