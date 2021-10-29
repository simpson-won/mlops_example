
import pandas as pd

from app.lib.preprocess_skl import PreprocessSkl
from app.config.config import PathConfig
from app.lib.model_skl import ModelingSkl

from app.lib.http_util import file_get


class TrainSkl(PreprocessSkl, PathConfig, ModelingSkl):

    __file_X = ''
    __file_y = ''

    def __init__(self):
        PreprocessSkl.__init__(self)
        PathConfig.__init__(self)
        ModelingSkl.__init__(self)
        self.__train_file_X = 'aimmo_skl_X_train.csv'
        self.__train_file_y = 'aimmo_skl_y_train.csv'
        self.__test_file_X = 'aimmo_skl_X_test.csv'
        self.__test_file_y = 'aimmo_skl_y_test.csv'
        self.__debug = False


    def get_train_data(self,
                       is_local:bool,
                       file_X:str,
                       file_y:str,
                       addr:str,
                       port:int):
        if is_local:
            X = pd.read_csv(file_X)
            y = pd.read_csv(file_y,squeeze=True)
        else:
            X = file_get(addr=addr,
                         port=port,
                         file_name=file_X)
            y = file_get(addr=addr,
                         port=port,
                         file_name=file_y,
                         is_series=True)
        return X, y


    def run(self, n_estimator: int=100,
            d_server_addr: str = '127.0.0.1',
            d_server_port: int = 80,
            d_server_token: str = 'xyz',
            is_local = True):

        train_X, train_y = self.get_train_data(
                                   is_local=is_local,
                                   file_X=self.__train_file_X,
                                   file_y=self.__train_file_y,
                                   addr=d_server_addr,
                                   port=d_server_port)

        test_X, test_y = self.get_train_data(
                                   is_local=is_local,
                                   file_X=self.__test_file_X,
                                   file_y=self.__test_file_y,
                                   addr=d_server_addr,
                                   port=d_server_port)

        if self.__debug:
            print('X =\n', str(type(train_X)) + '\n', train_X)
            print('y =\n', str(type(train_y)) + '\n', train_y)
            print('X =\n', str(type(test_X)) + '\n', test_X)
            print('y =\n', str(type(test_y)) + '\n', test_y)

        model, model_info, predict = self.run_modeling(n_estimator=n_estimator,
                                              train_X = train_X,
                                              train_y = train_y,
                                              test_X = test_X,
                                              test_y = test_y)
        print('Complete to make model.....')
        return model, model_info, predict

