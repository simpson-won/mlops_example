
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
        self.__file_X = 'aimmo_skl_X.csv'
        self.__file_y = 'aimmo_skl_y.csv'

    def run(self, n_estimator: int=100,
            d_server_addr: str = '127.0.0.1',
            d_server_port: int = 80,
            d_server_token: str = 'xyz',
            is_local = True):

        if is_local:
            X = pd.read_csv(self.__file_X)
            y = pd.read_csv(self.__file_y)
        else:
            X = file_get(self.__file_X)
            y = file_get(self.__file_y)
        #print('X =', type(X), X)
        #print('y =', type(y), y)
        model, model_info = self.run_modeling(X, y, n_estimator)
        return model, model_info

