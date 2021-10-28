
import pandas as pd

from app.lib.preprocess_skl import PreprocessSkl
from app.config.config import PathConfig
from app.lib.dataio import DataIOSteam
from app.lib.model_skl import ModelingSkl


class TrainSkl(PreprocessSkl, PathConfig, ModelingSkl, DataIOSteam):
    def __init__(self):
        PreprocessSkl.__init__(self)
        PathConfig.__init__(self)
        ModelingSkl.__init__(self)
        DataIOSteam.__init__(self)

    def run(self, n_estimator: int=100,
            d_server_addr: str = '127.0.0.1',
            d_server_port: int = 80,
            d_server_token: str = 'xyz'):
        is_local = True
        data = self._get_data(self.data_path, is_local=is_local)
        data = self.run_preprocessing(data)
        print('data =', data)
        X, y = self._get_X_y(data)
        print('X =', type(X), X)
        print('y =', type(y), y)
        #model, model_info = self.run_modeling(X, y, n_estimator)
        #return model, model_info

