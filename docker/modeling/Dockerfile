FROM python:3.8.10

RUN mkdir -p /root/mlops
ADD app /root/mlops
ADD data /root/mlops
ADD requirements.txt /root/mlops

RUN pip install -r /root/mlops/requirements.txt

WORKDIR /root/mlops



CMD ["python", "app/lib/main.py"]
