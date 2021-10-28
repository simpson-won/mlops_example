import argparse
import sys
import os

import mlflow
from mlflow import sklearn as ml_sklearn
from mlflow import log_artifacts
from mlflow import log_metric, log_metrics
from mlflow import log_param, log_params


from app.train.train_skl import TrainSkl

arguments = {
    'n_estimator':100,
    'mlflow_server_addr':'1',
    'mlflow_server_port':0,
    'experiment_name':'',
    'data_server_addr':'',
    'data_server_port':0,
    'data_server_token':''
}

def main(n_estimator:int ,
         experiment_name: str,
         server_addr: str,
         server_port: int,
         d_server_addr: str,
         d_server_port: int,
         d_server_token: str):
    #mlflow.set_experiment(experiment_name)
    #mlflow.set_tracking_uri(f'http://{server_addr}:{server_port}')

    trainSkl = TrainSkl()

    model, model_info = trainSkl.run(n_estimator=n_estimator,
                                     d_server_addr = d_server_addr,
                                     d_server_port = d_server_port,
                                     d_server_token = d_server_token)
    '''log metric을 하나하나 등록할 때는 아래와 같이 진행
        #log_metric("rf_score", score_info['rf_model_score'])
        #log_metric("lgbm_score", score_info['lgbm_model_score'])
    '''
    # metrics를 한 번에 등록 -> json 형태가 되어야 함
    #log_metrics(model_info['score'])
    #log_params(model_info['params'])

    #ml_sklearn.log_model(sk_model=model,
    #                     artifact_path="sklearn-model",
    #                     registered_model_name='ml_model')

    #print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    #mlflow.end_run()

def get_arg_parser():
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '--n_estimator', type=int, default=100
    )

    argument_parser.add_argument(
        '--mlflow_server_addr', type=str, default='127.0.0.1'
    )

    argument_parser.add_argument(
        '--mlflow_server_port', type=int, default=30100
    )

    argument_parser.add_argument(
        '--experiment_name', type=str, default='aimmo'
    )

    argument_parser.add_argument(
        '--data_server_addr', type=str, default='127.0.0.1'
    )

    argument_parser.add_argument(
        '--data_server_port', type=int, default=80
    )

    argument_parser.add_argument(
        '--data_server_token', type=str, default='f9403fc5f537b4ab332d'
    )

    args = argument_parser.parse_args()

    arguments['n_estimator'] = args.n_estimator
    arguments['mlflow_server_addr'] = args.mlflow_server_addr
    arguments['mlflow_server_port'] = args.mlflow_server_port
    arguments['experiment_name'] = args.experiment_name
    arguments['data_server_addr'] = args.data_server_addr
    arguments['data_server_port'] = args.data_server_port
    arguments['data_server_token'] = args.data_server_token


if __name__ == "__main__":

    get_arg_parser()

    main(n_estimator=arguments['n_estimator'],
         experiment_name=arguments['experiment_name'],
         server_addr=arguments['mlflow_server_addr'],
         server_port=arguments['mlflow_server_port'],
         d_server_addr=arguments['data_server_addr'],
         d_server_port=arguments['data_server_port'],
         d_server_token=arguments['data_server_token'])
