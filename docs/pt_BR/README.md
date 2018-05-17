# Relatórios para Python, com JasperReports.
[![Build Status](https://travis-ci.org/jadsonbr/pyreport.svg?branch=master)](https://travis-ci.org/jadsonbr/pyreport)
[![Coverage Status](https://coveralls.io/repos/github/jadsonbr/pyreport/badge.svg?branch=master)](https://coveralls.io/github/jadsonbr/pyreport?branch=master)
[![Code Health](https://landscape.io/github/jadsonbr/pyreport/master/landscape.svg?style=flat)](https://landscape.io/github/jadsonbr/pyreport/master)
[![PyPI](https://img.shields.io/pypi/l/pyreportjasper.svg)](https://github.com/jadsonbr/pyreport/blob/master/LICENSE)

**Traduções**

[![en_US](https://img.shields.io/badge/language-en__US-red.svg)](../../README.md)

**Está usando servidores Linux?**

Não se esqueça de conceder a permissão 777 para o diretório onde está o pacote.

##Introdução

Este pacote pretende ser uma solução para compilar e processar JasperReports (arquivos .jrxml e .jasper).

###Por quê?

Você já teve que criar um bom relatório com um monte de campos para o seu grande aplicativo da web ou desktop?

Eu precisei e as soluções lá fora não eram perfeitas. Gerando *HTML* + *CSS* para fazer um *PDF*? *WTF*? Isso não faz sentido! :)

Então eu encontrei **JasperReports** a melhor solução de código aberto para relatórios.

###O que posso fazer com isso?

Bem, tudo. JasperReports é uma ferramenta poderosa para **RELATÓRIO** e **BI**.

**De seu site:**

> A JasperReports Library é o mecanismo de geração de relatórios de código aberto mais popular do mundo. É inteiramente escrito em Java e é capaz de usar dados provenientes de qualquer tipo de fonte de dados e produzir documentos perfeitos que pode ser visualizado, impresso ou exportado em uma variedade de formatos de documentos, incluindo HTML, PDF, Excel, OpenOffice e Word .

Recomenda-se utilizar [Jaspersoft Studio](http://community.jaspersoft.com/project/jaspersoft-studio) para criar seus relatórios, conectá-lo à sua fonte de dados (ex:JSON, XML, MySQL, POSTGRES, SQL Server), e obter os resultados em PDF, XLS, DOC, RTF, ODF, etc.

*Alguns exemplos do que você pode fazer:*

* Invoices
* Reports
* Listings

Pacote para gerar relatórios com [JasperReports 6.3.1](http://community.jaspersoft.com/project/jasperreports-library) biblioteca através de [JasperStarter v3.1](https://sourceforge.net/projects/jasperstarter/files/JasperStarter-3.1/) ferramenta de linha de comando.

##Requisitos

* Java JDK 1.8
* Python [subprocess.run()](https://docs.python.org/3/library/subprocess.html) função

##Opcional

* [Mysql JDBC](http://dev.mysql.com/downloads/connector/j/) (Se você quiser usar o banco de dados)
* [PostgreSQL JDBC](https://jdbc.postgresql.org/download.html) (Se você quiser usar o banco de dados)
* [SQL Server JDBC](https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=11774) (Se você quiser usar o banco de dados)
* [Oracle JDBC](http://www.oracle.com/technetwork/apps-tech/jdbc-112010-090769.html) (Se você quiser usar o banco de dados)
* [Jaspersoft Studio](http://community.jaspersoft.com/project/jaspersoft-studio) (Para desenhar e compilar seus relatórios)

###Notas

* O driver JDBC de seu banco de dados deve ser colocado no diretório `pyjasper/jasperstarter/jdbc/`.
* Usando **pyjasper**, você também pode acessar diferentes tipos de fontes de dados, incluindo CSV, JDBC, JSON, NoSQL, XML ou sua própria fonte de dados personalizada.

###Java (JDK and JRE)

Verifique se você já possui o Java instalado:

```
$ javac -version
javac version 1.8.0_101
```

Se você obter:

    command not found: javac

Em seguida, instale-o com: (Ubuntu/Debian)

    $ sudo apt-get install default-jdk

Para instalar em: (centOS/Fedora)

    # yum install java-1.8.0-openjdk.x86_64

Para instalar em windows visite o link-> [JDK](http://www.oracle.com/technetwork/pt/java/javase/downloads/jdk8-downloads-2133151.html) e procure a versão mais apropriada para o seu sistema.

Agora execute o `javac -version` novamente e verifique se a saída está ok.

##Instalação

Instale [PyPI](https://pypi.python.org/pypi/pyreportjasper) se você não o tiver.
```
pip install pyreportjasper
```

e é isso.

##Exemplos

###O exemplo do *Hello World*.

Vá para o diretório de exemplos na raiz do pacote 
Abra o arquivo `test/examples/hello_world.jrxml` com o Jaspersoft Studio ou com o seu editor de texto favorito e dê uma olhada no código-fonte.

####Compilando

Primeiro precisamos compilar nosso arquivo `JRXML` em um arquivo binário` JASPER`. Só precisamos fazer isso uma vez.

**Nota 1:** Você não precisa fazer essa etapa se estiver usando *Jaspersoft Studio*. Você pode compilar diretamente dentro do programa.

```python
import os
import pyjasper

def compiling():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    jasper = pyjasper.JasperPy()
    jasper.compile(input_file)

```

Este comando compilará o arquivo fonte `hello_world.jrxml` para um arquivo` hello_world.jasper`.

####Processando

Agora vamos processar o relatório que compilamos antes:

```python
import os
import pyjasper

def processing():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file, output=output, format_list=["pdf", "rtf"])

```

Agora verifique a pasta de exemplos! :) Ótimo direito? Agora você tem 2 arquivos, `hello_world.pdf` e` hello_world.rtf`.

Verifique a *API* das funções `compile` e `process` no arquivo `pyjasper/jasperpy.py`.

####Listagem de parâmetros 

Consultando o arquivo jasper para examinar os parâmetros disponíveis no arquivo jasper (.jrxml):

```python
import os
import pyjasper

def listing_parameters():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world_params.jrxml'
    jasper = pyjasper.JasperPy()
    output = jasper.list_parameters(input_file)
    print(output)

```

###Exemplo avançado - usando um banco de dados

Também podemos especificar parâmetros para a conexão com o banco de dados:

```python
import os
from platform import python_version
import pyjasper

def advanced_example_using_database():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    con = {
        'driver': 'postgres',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'host': 'DB_HOST',
        'database': 'DB_DATABASE',
        'schema': 'DB_SCHEMA',
        'port': '5432'
    }
    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file,
        output=output,
        format_list=["pdf", "rtf", "xml"],
        parameters={'python_version': python_version()},
        db_connection=con,
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    )

```

**Nota 2:**

Para obter uma lista completa dos locais, consulte [Supported Locales](http://www.oracle.com/technetwork/java/javase/java8locales-2095355.html)


###Relatórios de um XML

Veja como é fácil gerar um relatório com uma origem de um arquivo XML:

```python
import os
import pyjasper

def xml_to_pdf():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/CancelAck.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_CancelAck'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/CancelAck.xml'

    jasper = pyjasper.JasperPy()

    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'xml',
            'xml_xpath': '/CancelResponse/CancelResult/ID',
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    )

    print('Result is the file below.')
    print(output + '.pdf')
    
```

###Relatórios de um arquivo JSON

Veja como é fácil gerar um relatório com uma fonte de um arquivo JSON:

```python
import os
import pyjasper

def json_to_pdf():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/json.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_Contacts'
    json_query = 'contacts.person'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/contacts.json'

    jasper = pyjasper.JasperPy()
    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'json',
            'json_query': json_query,
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    )

    print('Result is the file below.')
    print(output + '.pdf')
```

###Testes

Todos os testes estão no diretório `test`. Para executá-los.

```
python setup.py test
```

##Performance

Depende da complexidade, da quantidade de dados e dos recursos da sua máquina (deixe-me saber o seu caso de uso).

Eu tenho um relatório que gera um *Invoice* com uma conexão DB, imagens e várias páginas e leva cerca de **3/4 segundos** para processar. Eu sugiro que você use um trabalhador para gerar os relatórios em segundo plano.

##Questões?

Abrir uma [Issue](https://github.com/jadsonbr/pyreport/issues) 

##Contribuir

Contribuir para a comunidade Python, sinta-se livre para contribuir, fazer um fork!!

###Colaboradores

* Michell Stuttgart <michellstut@gmail.com>

##Obrigado

Graças a [Cenote GmbH](http://www.cenote.de/) pela biblioteca [JasperStarter](http://jasperstarter.sourceforge.net/).
