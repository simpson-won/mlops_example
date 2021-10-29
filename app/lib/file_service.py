############################################
#
#
#

import pandas as pd
from app.lib.http_util import file_get
from app.lib.panda_util import split_data

class FileService:

    def __init__(self):
        pass


    def get_data(self,
                 path:str,
                 testmode:str = 'train',
                 is_local:bool = True,
                 is_train:bool = True,
                 addr:str = '127.0.0.1',
                 port:int = 25478 ):
        filename = f'skl_{testmode}.csv'
        if is_local: 
            filepath = f'{path}/{filename}'
            data = pd.read_csv(filepath)
            df_train, df_test = split_data(data, test_ratio=0.3)
            if is_train:
                return df_train
            return df_test
        return self._get_train_data_from_remote(addr=addr,
                                                port=port,
                                                filename=filename)


    def _get_train_data_from_remote(self,
                                    addr:str = '127.0.0.1',
                                    port:int = 8001,
                                    filename:str = 'skl_train.csv'):

        return file_get(addr, port, filename)
        
    
