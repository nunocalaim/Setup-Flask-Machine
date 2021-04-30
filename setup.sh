#!/bin/sh

sudo add-apt-repository universe
sudo apt-get -y update
sudo apt -y install python3-pip
cd Setup-Flask-Machine/python_flask
pip3 install -r requirements.txt
pip3 install connexion[swagger-ui]
nohup python3 -m tracking_server &