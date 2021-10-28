
import pandas as pd

from preprocess_skl import TitanicPreprocessSkl
from config import PathConfig
from dataio import DataIOSteam
from model_skl import TitanicModelingSkl


class TitanicMain(TitanicPreprocessSkl, PathConfig, TitanicModelingSkl, DataIOSteam):
    def __init__(self):
        TitanicPreprocess.__init__(self)
        PathConfig.__init__(self)
        TitanicModeling.__init__(self)
        DataIOSteam.__init__(self)

    def run(self, n_estimator=100):
        data = self._get_data(self.titanic_path)
        data = self.run_preprocessing(data)
        X, y = self._get_X_y(data)
        model, model_info = self.run_sklearn_modeling(X, y, n_estimator)
        return model, model_info

