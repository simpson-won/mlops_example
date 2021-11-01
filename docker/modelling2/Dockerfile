FROM python:3.8.10

RUN mkdir -p /root/mlops
COPY * /root/mlops
RUN ls -al /root/mlops
COPY ../../app /root/mlops
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
