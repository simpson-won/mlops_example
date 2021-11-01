import sys
import os
import pandas as pd

from app import get_arg_parser, arguments

from app.lib.preprocess_skl import PreprocessSkl
from app.config.config import PathConfig
from app.lib.file_service import FileService
from app.lib.model_skl import ModelingSkl
from app.lib.panda_util import get_X_y
from app.lib.http_util import file_post, file_get


class Preprocess(PreprocessSkl, PathConfig, FileService):

    def __init__(self):
        PreprocessSkl.__init__(self)
        PathConfig.__init__(self)
        FileService.__init__(self)


    def preprocess(addr:str,
                   port:int,
                   path:str,
                   is_local:bool):
        data = self.get_data(addr=d_server_addr,
                             port=d_server_port,
                             path=self.data_path,
                             is_local=local_only)
        return self.run_preprocessing(data)


    def run(self,
            exp_name: str='aimmo',
            d_server_addr: str = '127.0.0.1',
            d_server_port: int = 80,
            d_server_token: str = 'xyz',
            local_only = True,
            delete_local = True):

        modes = ['train', 'test']

        for mode in modes:
            data = self.get_data(addr=d_server_addr,
                                 port=d_server_port,
                                 path=self.data_path,
                                 is_local=local_only,
                                 testmode=mode)
            data = self.run_preprocessing(data, mode=mode)

            X, y = get_X_y(data)

            ##############
            ###  debug
            ##############
            print('X=\n', str(type(X)) + '\n', X)
            print('y=\n', str(type(y)) + '\n', y)


            file_name_X = f'{exp_name}_skl_X_{mode}.csv'
            file_name_y = f'{exp_name}_skl_y_{mode}.csv'

            X.to_csv(file_name_X, index=False)
            y.to_csv(file_name_y, index=False)

            ## Send to File Server
            if local_only == False:
                file_post(addr=d_server_addr,
                          port=d_server_port,
                          file_name=file_name_X)
                file_post(addr=d_server_addr,
                          port=d_server_port,
                          file_name=file_name_y)

            if delete_local or local_only == False:
                os.remove(file_name_X)
                os.remove(file_name_y)


if __name__=="__main__":

    get_arg_parser()
    preprocess = Preprocess()

    preprocess.run(
         exp_name=arguments['exp_name'],
         d_server_addr=arguments['data_server_addr'],
         d_server_port=arguments['data_server_port'],
         d_server_token=arguments['data_server_token'],
         local_only=arguments['local_test'],
         delete_local=True)
