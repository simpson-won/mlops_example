FROM python:3.8.10

RUN mkdir -p /root/mlops/app
COPY app /root/mlops
COPY data /root/mlops
COPY requirements.txt /root/mlops
RUN ls -al

RUN pip install -r /root/mlops/requirements.txt

WORKDIR /root/mlops

RUN echo '############################'
RUN echo '##'
RUN echo '## RUN'
RUN echo '##'
RUN echo '############################'
RUN pwd

CMD ["python", "app/lib/main.py"]
