# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#

import os
import subprocess
import re
import xml.etree.ElementTree as ET

import tempfile
import jpyutil
import jpy
import json
from requests import Request, Session

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

    _FORMATS_JSON = ('pdf')

    _FORMATS_METHODS_REQUEST = ('GET', 'POST', 'PUT')

    def __init__(self, resource_dir=False, jvm_maxmem='512M', jvm_classpath=None):
        self.WINDOWS = True if os.name == 'nt' else False
        self.SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
        self.LIBS = os.path.join(self.SCRIPT_DIR, 'jasperstarter', 'lib')
        if not os.path.isdir(self.LIBS):
            raise NameError('Unable to find lib in {0}'.format(self.LIBS))
        self.CLASSPATH = os.path.join(self.LIBS, 'jasperstarter.jar')
        if not os.path.exists(self.CLASSPATH):
            raise NameError('Unable to find jasperstarter in {0}'.format(self.LIBS))
        if jvm_classpath is None:
            jpyutil.init_jvm(jvm_maxmem=jvm_maxmem, jvm_classpath=[self.CLASSPATH])
        else:
            jpyutil.init_jvm(jvm_maxmem=jvm_maxmem, jvm_classpath=[self.CLASSPATH, jvm_classpath])

        self.jvFile = jpy.get_type('java.io.File')
        self.jvArrays = jpy.get_type('java.util.Arrays')
        self.jvReport = jpy.get_type('de.cenote.jasperstarter.Report')
        self.jvConfig = jpy.get_type('de.cenote.jasperstarter.Config')
        self.jvDsType = jpy.get_type('de.cenote.jasperstarter.types.DsType')
        self.jvApplicationClasspath = jpy.get_type('de.cenote.tools.classpath.ApplicationClasspath')
        self.jvHashMap = jpy.get_type('java.util.HashMap')
        self.jvLocale = jpy.get_type('java.util.Locale')
        self.jvJasperFillManager = jpy.get_type('net.sf.jasperreports.engine.JasperFillManager')
        self.jvDb = jpy.get_type('de.cenote.jasperstarter.Db')
        self.jvJsonQueryExecuterFactory = jpy.get_type('net.sf.jasperreports.engine.query.JsonQueryExecuterFactory')
        self.jvJasperExportManager = jpy.get_type('net.sf.jasperreports.engine.JasperExportManager')


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

            if 'csv_first_row' in db_connection:
                command += ' --csv-first-row '

            if 'csv_columns' in db_connection:
                command += ' --csv-columns ' + db_connection['csv_columns']

            if 'csv_record_del' in db_connection:
                command += ' --csv-record-del="' + db_connection['csv_record_del'] + '"'

            if 'csv_field_del' in db_connection:
                command += ' --csv-field-del="' + db_connection['csv_field_del'] + '"'

            if 'csv_charset' in db_connection:
                command += ' --csv-charset=' + db_connection['csv_charset']

        if resource != "":
            if resource == ".":
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
                    self.command, shell=True, check=True, encoding='utf-8', stderr=subprocess.PIPE).returncode
            except AttributeError:
                output = subprocess.check_call(self.command, shell=True)
            except subprocess.CalledProcessError as e:
                raise NameError('Your report has an error and couldn\'t be processed!\n' + e.stderr)
        else:
            raise NameError('Invalid resource directory!')

        return output


    def process_json(self, input_file, output_file=False, format_list=['pdf'],
                parameters={}, connection={}, locale=False, resource=""):

        with tempfile.TemporaryDirectory() as tmp_dir:
            if not input_file:
                raise NameError('No input file!')

            if isinstance(format_list, list):
                if any([key not in self._FORMATS_JSON for key in format_list]):
                    raise NameError('Invalid format output!')
            else:
                raise NameError("'format_list' value is not list!")

            try:
                config = self.jvConfig()
                config.setInput(input_file)
                if locale:
                    config.setLocale(locale)
                if output_file:
                    config.setOutput(output_file)
                else:
                    list_patch = input_file.split('/')
                    list_name_extesion = list_patch[-1].split('.')
                    name_file = list_name_extesion[0]
                    file_out = os.path.join(os.path.dirname(input_file), name_file + '.jasper')
                    output_file = os.path.join(os.path.dirname(input_file), name_file + '.pdf')
                    config.setOutput(os.path.dirname(input_file))
                config.setOutputFormats(self.jvArrays.asList(format_list))
                if len(parameters) > 0:
                    config.setParams(self.jvArrays.asList([k + '=' + v for k, v in parameters.items()]))
                if 'driver' in connection:
                    if connection['driver'] == 'json':
                        config.setDbType(self.jvDsType.json)
                    elif connection['driver'] == 'jsonql':
                        config.setDbType(self.jvDsType.jsonql)
                else:
                    config.setDbType(self.jvDsType.none)

                if len(connection) > 0:
                    if 'data_file' not in connection and 'url_file' not in connection:
                        raise NameError('No data sources were reported')

                    if 'data_file' in connection:
                        config.setDataFile(self.jvFile(connection['data_file']))

                    if 'url_file' in connection:
                        try:
                            if isinstance(connection['url_method'], str):
                                if connection['url_method'] not in self._FORMATS_METHODS_REQUEST:
                                    raise NameError('Invalid method request!')
                            else:
                                raise NameError("'url_method' value is not list!")

                            PARAMS = connection['url_params'] if 'url_params' in connection else {}
                            DATA = connection['url_data'] if 'url_data_post' in connection else {}
                            HEADER = connection['url_header'] if 'url_header' in connection else {}

                            if 'url_method' in connection:
                                s = Session()
                                prepped = Request(
                                    connection['url_method'],
                                    connection['url_file'],
                                    data=DATA,
                                    headers=HEADER,
                                    params=PARAMS
                                ).prepare()
                                resp = s.send(request=prepped)
                            if resp.status_code == 200:
                                data = resp.json()
                                file_json = os.path.join(tmp_dir, 'data_report.json')
                                with open(file_json, 'w') as file:
                                    file.write(json.dumps(data))
                                config.setDataFile(self.jvFile(file_json))
                            else:
                                raise NameError('Error request status code: %s' % str(resp.status_code))
                        except Exception as e:
                            raise NameError('Error request: %s' % str(e))

                    if 'json_query' in connection:
                        config.setJsonQuery(connection['json_query'])

                    if 'jsonql_query' in connection:
                        config.setJsonQLQuery(connection['jsonql_query'])

                if os.path.isfile(resource):
                    self.jvApplicationClasspath.add(os.path.dirname(resource))
                elif os.path.isdir(resource):
                    self.jvApplicationClasspath.add(resource)

                report = self.jvReport(config, self.jvFile(config.getInput()))
                self.compile(input_file)
                parameters = self.jvHashMap()
                if config.hasAskFilter():
                    reportParams = config.getParams()
                    parameters = report.promptForParams(reportParams, parameters, report.jasperReport.getName())
                try:
                    if self.jvDsType.jsonql.equals(config.getDbType()):
                        db = self.jvDb()
                        ds = db.getJsonQLDataSource(config)
                        if 'json_locale' in connection:
                            parameters.put(self.jvJsonQueryExecuterFactory.JSON_LOCALE,
                                           self.jvLocale(connection['json_locale']))

                        if 'json_date_pattern' in connection:
                            parameters.put(self.jvJsonQueryExecuterFactory.JSON_DATE_PATTERN,
                                           self.jvLocale(connection['json_date_pattern']))

                        if 'json_number_pattern' in connection:
                            parameters.put(self.jvJsonQueryExecuterFactory.JSON_NUMBER_PATTERN,
                                           self.jvLocale(connection['json_number_pattern']))

                        if 'json_time_zone' in connection:
                            parameters.put(self.jvJsonQueryExecuterFactory.JSON_TIME_ZONE,
                                           self.jvLocale(connection['json_time_zone']))

                        jasperPrint = self.jvJasperFillManager.fillReport(file_out, parameters, ds)
                        self.jvJasperExportManager.exportReportToPdfFile(jasperPrint, output_file)
                    else:
                        raise NameError('Invalid json input!')
                except Exception as e:
                    raise NameError('Error: %s' % str(e))

                return 0
            except Exception as e:
                raise NameError('Error: %s' % str(e))

