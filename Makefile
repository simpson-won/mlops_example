# Makefile for mlflow-example
#
# 2021/10/26
###########################

.PHONY: clean install tests run all


clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

run-api:
	RUN="dev" PYTHONPATH=${PWD} gunicorn app.run_api:app -b 0.0.0.0:8080 -w 3

run-train:
	RUN="dev" PYTHONPATH=${PWD} python app/train/main.py
