import sys
import os

from app import get_arg_parser, arguments

import mlflow
from mlflow import sklearn as ml_sklearn
from mlflow import log_artifacts
from mlflow import log_metric, log_metrics
from mlflow import log_param, log_params


from app.train.train_skl import TrainSkl


def main(n_estimator:int ,
         exp_name: str,
         server_addr: str,
         server_port: int,
         d_server_addr: str,
         d_server_port: int,
         d_server_token: str,
         is_local_only = True):

    if is_local_only == False:
        print(f'exp_name = {exp_name}')
        mlflow.set_experiment(exp_name)
        mlflow.set_tracking_uri(f'http://{server_addr}:{server_port}')

    trainSkl = TrainSkl()

    model, model_info, predict = trainSkl.run(n_estimator=n_estimator,
                                     d_server_addr = d_server_addr,
                                     d_server_port = d_server_port,
                                     d_server_token = d_server_token,
                                     is_local = is_local_only)

    if is_local_only == False:
        log_metrics(model_info['score'])
        log_params(model_info['params'])

        log_metric('rmse', predict['rmse'])
        log_metric('r2', predict['r2'])
        log_metric('mae', predict['mae'])


        ml_sklearn.log_model(sk_model=model,
                             artifact_path="sklearn-model",
                             registered_model_name='ml_model')

        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
        mlflow.end_run()


if __name__ == "__main__":

    get_arg_parser()

    main(n_estimator=arguments['n_estimator'],
         exp_name=arguments['exp_name'],
         server_addr=arguments['mlflow_server_addr'],
         server_port=arguments['mlflow_server_port'],
         d_server_addr=arguments['data_server_addr'],
         d_server_port=arguments['data_server_port'],
         d_server_token=arguments['data_server_token'],
         is_local_only=arguments['local_test'])
