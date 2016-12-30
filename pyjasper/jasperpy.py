# -*- coding: utf-8 -*-
import os
import subprocess

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


class JasperPy:
    """
    Author: Jadson Bonfim Ribeiro
    E-mail: jadsonbr@outlook.com.br
    """

    def __init__(self, resource_dir=False, redirect_output=False,
                 background=False):

        self.path_executable = os.path.dirname(os.path.abspath(__file__)) \
                               + '/jasperstarter/bin'

        self.windows = True if os.name == 'nt' else False
        self.the_command = ''
        self.redirect_output = redirect_output
        self.background = background

        if not resource_dir:
            resource_dir = os.path.dirname(os.path.abspath(__file__)) \
                           + '/jasperstarter/bin'
        else:
            if not os.path.exists(resource_dir):
                raise NameError('Invalid resource directory!')

        # Path to report resource dir or jar file
        self.resource_directory = resource_dir  

    def compile(self, input_file, output_file=False, background=True,
                redirect_output=True):

        if (input_file is None) or (not input_file):
            raise NameError('No input file')

        command = EXECUTABLE if self.windows \
            else self.path_executable + '/' + EXECUTABLE

        command += ' compile '
        command += "\"%s\"" % input_file

        if output_file is not False:
            command += ' -o ' + "\"%s\"" % output_file

        self.redirect_output = redirect_output
        self.background = background
        self.the_command = command

        return self

    def process(self, input_file, output_file=False, format_list=['pdf'],
                parameters={}, db_connection={}, locale='pt_BR',
                background=True, redirect_output=True):

        if (input_file is None) or (not input_file):
            raise NameError('No input file')

        if isinstance(format_list, list):
            if any([key not in FORMATS for key in format_list]):
                raise NameError('Invalid format!')
        else:
            raise NameError('Invalid format!')

        command = EXECUTABLE if self.windows \
            else self.path_executable + '/' + EXECUTABLE

        command += " --locale %s" % locale
        command += ' process '
        command += "\"%s\"" % input_file

        if output_file is not False:
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

        self.redirect_output = redirect_output
        self.background = background
        self.the_command = command
        return self

    def list_parameters(self, input_file):
        if not input_file:
            raise NameError('No input file')

        command = EXECUTABLE if self.windows \
            else self.path_executable + '/' + EXECUTABLE
        command += ' list_parameters '
        command += "\"%s\"" % input_file
        self.the_command = command

        return self

    def output(self):
        return self.the_command

    def execute(self, run_as_user=False):

        if (run_as_user is not False) and (not self.windows):
            self.the_command = 'su -u ' + run_as_user + " -c \"" + \
                               self.the_command + "\""

        if os.path.isdir(self.path_executable):
            try:
                output = subprocess.run(
                    self.the_command, shell=True, check=True)
            except AttributeError:
                output = subprocess.check_call(self.the_command, shell=True)
            except subprocess.CalledProcessError as e:
                print(e.output)
                raise NameError('Your report has an error and couldn '
                                '\'t be processed!\ Try to output the command '
                                'using the function `output();` and run it '
                                'manually in the console.')
        else:
            raise NameError('Invalid resource directory.')

        return output
