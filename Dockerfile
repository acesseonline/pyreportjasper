FROM python:3.8-alpine

WORKDIR /opt/pyreportjasper_tests

RUN apk update \
        && apk upgrade \
        && apk add --no-cache bash \
        && apk add --no-cache --virtual=build-dependencies unzip \
        && apk add --no-cache curl \
        && apk add --no-cache ttf-dejavu \
        && apk add --no-cache openjdk19-jre

RUN apk update && apk add python3-dev \
                          gcc \
                          g++ \
                          libc-dev \
                          libffi-dev

RUN apk add --no-cache python3 \
        && python3 -m ensurepip \
        && pip3 install --upgrade pip setuptools \
        && rm -r /usr/lib/python*/ensurepip && \
        if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
        if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
        rm -r /root/.cache

RUN pip3 install pyproject coveralls requests pathlib jpype1

ENV LD_LIBRARY_PATH=/usr/lib/jvm/java-19-openjdk/lib/server
ENV JAVA_HOME=/usr/lib/jvm/java-19-openjdk/bin/java

ENV PYTHONPATH=/opt/pyreportjasper_tests:/opt/pyreportjasper_tests
ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python", "-m", "unittest", "discover", "./tests", "-p", "*.py"]
