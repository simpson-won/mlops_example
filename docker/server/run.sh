#!/bin/sh

set -e

STORE_URL='sqlite:///model.db'
ARTIFACT_ROOT='ftp://mlflow:mlflow@127.0.0.1/artifacts'
#ARTIFACT_ROOT='ftp://mlflow:mlflow@192.168.0.34/artifacts'
#ARTIFACT_ROOT='/mlflow/artifacts'

echo "store_uri="$STORE_URL
echo "artifacts_uri="$ARTIFACT_ROOT

mlflow server \
    --backend-store-uri $STORE_URL\
    --default-artifact-root $ARTIFACT_ROOT\
    --host 0.0.0.0 \
    --port $MLFLOW_PORT

