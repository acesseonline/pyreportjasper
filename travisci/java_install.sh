#!/bin/bash

# show current JAVA_HOME and java version
echo ">>>>> Current JAVA_HOME: $JAVA_HOME <<<<<"
echo ">>>>> Current java -version: <<<<<"
java -version

# install Java 8
echo ">>>>> Add repository <<<<<"
sudo add-apt-repository -y ppa:openjdk-r/ppa
echo ">>>>> Update repository <<<<<"
sudo apt-get -qq update
echo ">>>>> Install open jdk 11 <<<<<"
sudo apt-get install -y openjdk-11-jdk

# change JAVA_HOME to Java 11
echo ">>>>> Set variable JAVA_HOME <<<<<"
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64