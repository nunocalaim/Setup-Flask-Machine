# 

run the following command:
swagger-codegen generate -i swagger.yml -l python-flask -c config.json -o python_flask 

substitute python_flask/tracking_server/controllers/default_controller.py by default_controller.py
substitute python_flask/tracking_server/controllers/util.py by util.py

```
cd python_flask
pip3 install -r requirements.txt
python3 -m tracking_server
test.sh
```

