# Instructions

This repo is used to create a Flask server that communicates with a private s3 bucket.

All aws resources are assumed to be provisioned, then you should ssh to your instance and run these commands in order


```
sudo add-apt-repository universe
sudo apt-get -y update
sudo apt -y install python3-pip
cd Setup-Flask-Machine/python_flask
pip3 install -r requirements.txt
pip3 install connexion[swagger-ui]
nohup python3 -m tracking_server &
```

