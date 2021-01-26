#!/bin/bash
​
sudo apt-get -y update
sudo apt-get -y upgrade

# Python
sudo apt-get install python3.6
sudo apt-get install python3-pip -y

# Import programs
cp /vagrant/KeyDerivations.py .
cp /vagrant/EncryptDecrypt.py .

## Test python with :
# python3 --version
# pip3 --version

## Install Python moduls :
# pip3 install bitcoin

# pip3 install bitcoin
# python3.6 KeyDerivations.py
# python3.6 EncryptDecrypt.py

echo "************"
echo "INSTALL DONE"
echo "************"