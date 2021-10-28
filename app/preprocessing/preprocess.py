import argparse
import sys
import os
import pandas as pd

from app.lib.preprocess_skl import PreprocessSkl
from app.config.config import PathConfig
from app.lib.file_service import FileService
from app.lib.model_skl import ModelingSkl
from app.lib.panda_util import get_X_y
from app.lib.http_util import file_post, file_get


arguments = {
    'experiment_name':'',
    'data_server_addr':'',
    'data_server_port':0,
    'data_server_token':''
}


def get_arg_parser():
    argument_parser = argparse.ArgumentParser()

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

    arguments['experiment_name'] = args.experiment_name
    arguments['data_server_addr'] = args.data_server_addr
    arguments['data_server_port'] = args.data_server_port
    arguments['data_server_token'] = args.data_server_token


class Preprocess(PreprocessSkl, PathConfig, FileService):

    def __init__(self):
        PreprocessSkl.__init__(self)
        PathConfig.__init__(self)
        FileService.__init__(self)

    def run(self,
            exp_name: str='aimmo',
            d_server_addr: str = '127.0.0.1',
            d_server_port: int = 80,
            d_server_token: str = 'xyz',
            local_only = True,
            delete_local = True):

        is_local = True
        data = self._get_data(self.data_path, is_local=is_local)
        data = self.run_preprocessing(data)

        X, y = get_X_y(data)

        file_name_X = exp_name + '_skl_X.csv'
        file_name_y = exp_name + '_skl_y.csv'

        X.to_csv(file_name_X)
        y.to_csv(file_name_y)

        ## Send to File Server
        if local_only == False:
            file_post(file_name_X)
            file_post(file_name_y)

        if delete_local:
            os.remove(file_name_X)
            os.remove(file_name_y)


if __name__=="__main__":

    get_arg_parser()
    preprocess = Preprocess()

    preprocess.run(
         exp_name=arguments['experiment_name'],
         d_server_addr=arguments['data_server_addr'],
         d_server_port=arguments['data_server_port'],
         d_server_token=arguments['data_server_token'],delete_local = False)
