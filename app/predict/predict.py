###########################
# predict.py
#
# api server

import mlflow
import pandas as pd
import json

from app.config import API_CONFIG_REMOTE as conf
#from app.config import API_CONFIG_LOCAL as conf

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route("/ml/hello")
def hello():
    return "hello."

@app.route("/ml/predict", methods=['POST'])
def predict():
    content = request.json
    print(content)

    if "key" not in content:
        return abort(400, 'Record not found')

    model_key = content['key']
    data = content['data']

    model_uri = f'runs:/{content["key"]}/sklearn-model'

    print('model_uri =', model_uri)

    mlflow.set_experiment('aimmo')
    mlflow_addr = conf['mlflow']['addr']
    mlflow_port = conf['mlflow']['port']
    mlflow_uri = f'http://{mlflow_addr}:{mlflow_port}'
    mlflow.set_tracking_uri(mlflow_uri)

    with mlflow.start_run():
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        predicted = loaded_model.predict(pd.DataFrame(data))
        ans = {'code':200, 
               'predicted': predicted.tolist(),
               'req-uri':model_uri,
               'mlflow-uri':mlflow_uri}
        return jsonify(ans)
    return abort(500, 'Fail to predict')

