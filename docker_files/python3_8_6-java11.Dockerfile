FROM python:3.8.6-buster

WORKDIR /opt/pyreportjasper

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

RUN set -e; \
    pip3 install coveralls
RUN set -e; \
    pip3 install coveralls
RUN set -e; \
    pip3 install pathlib
RUN set -e; \
    pip3 install requests
RUN set -e; \
    pip install JPype1

COPY . .

ENV PYTHONPATH=/opt/pyreportjasper:/opt/pyreportjasper/pyreportjasper
ENV PYTHONUNBUFFERED=1

CMD ["coverage", "run", "setup.py", "test"]
