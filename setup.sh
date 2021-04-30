#!/bin/sh

sudo add-apt-repository universe
sleep 5
sudo apt-get -y update
sleep 40
sudo apt -y install python3-pip
sleep 15
cd Setup-Flask-Machine/python_flask
sleep 5
pip3 install -r requirements.txt
sleep 5
pip3 install connexion[swagger-ui]
sleep 5
nohup python3 -m tracking_server &