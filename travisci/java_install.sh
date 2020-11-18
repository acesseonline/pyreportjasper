#!/bin/bash

# show current JAVA_HOME and java version
echo ">>>>> Current JAVA_HOME: $JAVA_HOME <<<<<"
echo ">>>>> Current java -version: <<<<<"
java -version

# install Java 15
echo ">>>>> Add repository <<<<<"
sudo add-apt-repository ppa:linuxuprising/java
echo ">>>>> Update repository <<<<<"
sudo apt-get -qq update
echo ">>>>> Install jdk 15 <<<<<"
sudo apt install -y oracle-java15-set-default
echo oracle-java15-installer shared/accepted-oracle-license-v1-2 select true | sudo /usr/bin/debconf-set-selections


echo "*********************************"
java -version
echo "*********************************"