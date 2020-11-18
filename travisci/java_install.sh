#!/bin/bash

# show current JAVA_HOME and java version
echo "Current JAVA_HOME: $JAVA_HOME"
echo "Current java -version:"
java -version

# install Java 8
sudo add-apt-repository -y ppa:openjdk-r/ppa
sudo apt-get -qq update
sudo apt-get install -y openjdk-11-jdk --no-install-recommends
sudo update-alternatives --config java

# change JAVA_HOME to Java 11
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64