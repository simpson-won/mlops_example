FROM python:3.8.10

RUN uname -a
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install sqlite3=3.*

RUN pip install mlflow

RUN mkdir -p /mlflow/artifacts
COPY run.sh /mlflow
RUN chmod 777 -fR /mlflow

WORKDIR /mlflow

RUN ls -al
ENV MLFLOW_PORT 5003

ENTRYPOINT ["./run.sh"]

