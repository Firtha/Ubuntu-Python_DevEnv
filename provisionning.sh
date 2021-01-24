#!/bin/bash
​
sudo apt-get -y update
sudo apt-get -y upgrade

# Python
sudo apt-get install python3.6
sudo apt-get install python3-pip -y

# Import program
cp /vagrant/Cryptography-TP.py . 

## Test python with :
# python3 --version
# pip3 --version

# pip3 install bitcoin
# python3.6 Cryptography-TP.py

echo "************"
echo "INSTALL DONE"
echo "************"