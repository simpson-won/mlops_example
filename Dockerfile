FROM python:3.8.10

RUN mkdir -p /root/mlops/app
RUN mkdir -p /root/mlops/data
COPY app /root/mlops/app
COPY data /root/mlops/data
COPY requirements.txt /root/mlops
RUN ls -al /root/mlops

RUN pip install -r /root/mlops/requirements.txt

WORKDIR /root/mlops

RUN echo '############################'
RUN echo '##'
RUN echo '## RUN'
RUN echo '##'
RUN echo '############################'
RUN pwd

CMD ["python", "app/lib/main.py"]
