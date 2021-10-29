import argparse
import sys
import os


arguments = {
    'n_estimator':100,
    'mlflow_server_addr':'1',
    'mlflow_server_port':0,
    'exp_name':'',
    'data_server_addr':'',
    'data_server_port':0,
    'data_server_token':'',
    'local_test':True,
    'model_code':''
}


def get_arg_parser():
    argument_parser = argparse.ArgumentParser()

    parameters = [
        ['--n_estimator', int, 100],
        ['--mlflow_server_addr', str, '127.0.0.1'],
        ['--mlflow_server_port', int, 30100],
        ['--exp_name', str, 'aimmo'],
        ['--data_server_addr', str, '127.0.0.1'],
        ['--data_server_port', int, 80],
        ['--data_server_token', str, 'f9403fc5f537b4ab332d'],
        ['--local_test', str, 'True'],
        ['--model_code', str, '']]

    for parameter in parameters:
        argument_parser.add_argument(
            parameter[0], type=parameter[1], default=parameter[2])

    args = argument_parser.parse_args()

    arguments['n_estimator'] = args.n_estimator
    arguments['mlflow_server_addr'] = args.mlflow_server_addr
    arguments['mlflow_server_port'] = args.mlflow_server_port
    arguments['exp_name'] = args.exp_name
    arguments['data_server_addr'] = args.data_server_addr
    arguments['data_server_port'] = args.data_server_port
    arguments['data_server_token'] = args.data_server_token
    arguments['local_test'] = True if args.local_test == "True" else False
    arguments['model_code'] = args.model_code

