
import os
import string
import subprocess


class JasperPy:
    """
    Author: Jadson Bonfim Ribeiro
    E-mail: jadsonbr@outlook.com.br
    """

    executable = 'jasperstarter'
    path_executable = ''
    resource_directory = ''
    windows = False
    the_command = ''
    redirect_output = True
    background = True

    formats = ['pdf', 'rtf', 'xls', 'xlsx', 'docx', 'odt', 'ods', 'pptx', 'csv', 'html', 'xhtml', 'xml', 'jrprint']
    resource_directory = ''  # Path to report resource dir or jar file

    def __init__(self, resource_dir=False):
        self.path_executable = os.path.dirname(os.path.abspath(__file__)) + '/jasperstarter/bin'
        if os.name == 'nt':
            self.windows = True        
        if not resource_dir:
            self.resource_dir = os.path.dirname(os.path.abspath(__file__)) + '/jasperstarter/bin'            
        else:
            if not os.path.exists(resource_dir):
                raise NameError('Invalid resource directory.')
        self.resource_directory = resource_dir
            

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")      


    def compile(self,input_file, output_file=False, background=True, redirect_output=True):
        if (input_file is None) or (not input_file):
            raise NameError('No input file')
        command = self.executable if self.windows else self.path_executable +'/'+ self.executable
        command += ' compile '
        command += "\"%s\"" % (input_file)
        if output_file != False:
            command += ' -o ' + "\"%s\"" % (output_file)

        self.redirect_output = redirect_output
        self.background = background
        self.the_command = command
        return self


    def process(self, input_file, output_file=False, format=['pdf'], parameters={}, db_connection={}, locale='pt_BR', background=True, redirect_output=True):
        if (input_file is None) or (not input_file):
            raise NameError('No input file')

        if isinstance(format, list)	:
            for key in format:
                if not key in self.formats:
                    raise NameError('Invalid format!')
        else:
            if not format in self.formats:
                raise NameError('Invalid format!')

        command = self.executable if self.windows else self.path_executable +'/'+ self.executable
        command += " --locale %s" % (locale)       
        command += ' process '
        command += "\"%s\"" % (input_file)
        if output_file != False:
            command += ' -o ' + "\"%s\"" % (output_file)
        if isinstance(format, list):
            command += ' -f '+ "".join(format)
        else:
            command += ' -f '+ "".join(format)

        if len(parameters) > 0:
            command += ' -P '
            for key, value in parameters.items():
                param = key + '="' + value + '" '
                command += " " + param + " "
        if len(db_connection) > 0:
            command += ' -t ' + db_connection['driver']

            if db_connection['username']:
                command += " -u " + db_connection['username']

            if db_connection['password'] and not db_connection['password']:
                command += ' -p ' + db_connection['password']

            if db_connection['host'] and not db_connection['host']:
                command += ' -H ' + db_connection['host']

            if db_connection['database'] and not db_connection['database']:
                command += ' -n ' + db_connection['database']

            if db_connection['port'] and not db_connection['port']:
                command += ' --db-port ' + db_connection['port']

            if db_connection['jdbc_driver'] and not db_connection['jdbc_driver']:
                command += ' --db-driver ' + db_connection['jdbc_driver']

            if db_connection['jdbc_url'] and not db_connection['jdbc_url']:
                command += ' --db-url ' + db_connection['jdbc_url']

            if db_connection['jdbc_dir'] and not db_connection['jdbc_dir']:
                command += ' --jdbc-dir ' + db_connection['jdbc_dir']

            if db_connection['db_sid'] and not db_connection['db_sid']:
                command += ' --db-sid ' + db_connection['db_sid']

            if db_connection['xml_xpath']:
                command += ' --xml-xpath ' + db_connection['xml_xpath']

            if db_connection['data_file']:
                command += ' --data-file ' + db_connection['data_file']

            if db_connection['json_query']:
                command += ' --json-query ' + db_connection['json_query']

        self.redirect_output = redirect_output
        self.background = background
        self.the_command = command
        return self


    def list_parameters(self,input_file):
        if not input_file :
            raise NameError('No input file')
        command = executable if self.windows else self.path_executable +'/'+ self.executable
        command += ' list_parameters '
        command += "\"%s\"" % (input_file)
        self.the_command = command
        return self


    def output(self):
        return self.the_command


    def execute(self,run_as_user=False):
        if (run_as_user != False) and (not self.windows) :
            self.the_command = 'su -u ' + run_as_user + " -c \"" + self.the_command + "\""
        if os.path.isdir(self.path_executable):
            try:
                output = subprocess.run(self.the_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(e.message)
                raise NameError('Your report has an error and couldn \'t be processed!\ Try to output the command using the function `output();` and run it manually in the console.')
        else:
            raise NameError('Invalid resource directory.')

        return output

