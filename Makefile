# Makefile for mlflow-example
#
# 2021/10/26
###########################

.PHONY: clean install tests run all


clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

run-api:
	PYTHONPATH=${PWD} gunicorn app.predict.predict:app -b 0.0.0.0:5010 -w 3

run-train:
	RUN="dev" PYTHONPATH=${PWD} python app/train/main.py --data_server_addr=192.168.0.34 --data_server_port=8091 --local_test=False --mlflow_server_addr=192.168.0.24 --mlflow_server_port=30100 --n_estimator=50 --exp_name='aimmo'

run-preprocess:
	RUN="dev" PYTHONPATH=${PWD} python app/preprocessing/preprocess.py --data_server_addr=192.168.0.34 --data_server_port=8091 --local_test=False

run-data:
	PYTHONPATH=${PWD} python app/lib/http_util.py --data_server_addr=192.168.0.34 --data_server_port=8091 --local_test=False
