# 

run the following command:
swagger-codegen generate -i swagger.yml -l python-flask -c config.json -o python_flask 

substitute tracking_server/tracking_server/controllers/default_controller.py by default_controller.py

```
cd tracking_server
pip3 install -r python_flask/requirements.txt
python3 -m python_flask/tracking_server
```

