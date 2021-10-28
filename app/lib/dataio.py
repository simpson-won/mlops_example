############################################
#
#
#

import pandas as pd
from app.lib.get_data import file_get
from app.lib.panda_util import split_data

class DataIOSteam:

    def __init__(self):
        self.train_file_name = 'skl_train.csv'
        self.test_file_name = 'ske_test.csv'


    @property
    def train_file_name(self): 
        return self._train_file_name


    @property
    def test_file_name(self):
        return self._test_file_name


    @train_file_name.setter
    def train_file_name(self, name: str):
        self._train_file_name = name


    @test_file_name.setter
    def test_file_name(self, name: str):
        self._test_file_name = name


    def _get_data(self, path, is_local: bool = True, is_train: bool = True):
        print('_get_data 0', is_local, is_train)
        if is_local: 
            print('_get_data 1')
            filepath = f'{path}/{self.train_file_name}'
            print('_get_data 2', filepath)
            data = pd.read_csv(filepath)
            df_train, df_test = split_data(data, test_ratio=0.3)
            if is_train:
                return df_train
            print('_get_data 3')
            return df_test
        print('_get_data 4')
        return self._get_train_data_from_remote(is_train)

    def _get_train_data_from_remote(self, is_train: bool = True):
        if is_train:
            return file_get(self.train_file_name)
        return file_get(self.test_file_name)
        
    
    def _get_X_y(self, data):
        X = data[data.columns[1:]]
        X = X[['Sex', 'Age_band', 'Pclass']]
        y = data['Survived']

        return X, y
