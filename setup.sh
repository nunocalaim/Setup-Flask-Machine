#!/bin/sh

sudo add-apt-repository universe
sleep 10
echo "Added Repository Universe"
sudo apt-get -y update
sleep 40
echo "Updated apps"
sudo apt -y install python3-pip
sleep 40
echo "installed pip3"
cd Setup-Flask-Machine/python_flask
sleep 4
echo "changed directory"
pip3 install -r requirements.txt
sleep 20
echo "installed requirements"
pip3 install connexion[swagger-ui]
sleep 10
echo "Installed UI, starting Server now"
nohup python3 -m tracking_server &