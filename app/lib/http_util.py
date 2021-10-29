import requests
import pandas as pd
from io import StringIO
import os

from app import get_arg_parser, arguments

from app.lib.panda_util import split_data

params={'token':'f9403fc5f537b4ab332d'}

up_files = ['skl_train.csv', 'skl_test.csv']

all_data_file_name = 'skl_test_data.csv'


def file_post(addr:str, port:int, file_name:str):
    """
    post file to file server

    param file_name, str
    """
    handle = open(file_name, 'rb')
    upload = {'file': handle}

    up_uri = f'http://{addr}:{port}/upload'
    res = requests.post(url=up_uri, params=params, files=upload)

    return res


def file_get(addr:str, port:int, file_name:str, is_series:bool = False):
    """
    get file from file server


    param file_name, str
    """
    down_uri = f'http://{addr}:{port}/files/{file_name}'
    r = requests.get(url=down_uri, params=params)
    if is_series:
        df = pd.read_csv(StringIO(r.text), squeeze=True)
    else:
        df = pd.read_csv(StringIO(r.text))

    return df


if __name__=="__main__":

    get_arg_parser()

    df = file_get(addr=arguments['data_server_addr'],
                  port=arguments['data_server_port'],
                  file_name=all_data_file_name)

    df_train, df_test = split_data(df, 0.33)

    df_train.to_csv(up_files[0], index=False)
    df_test.to_csv(up_files[1], index=False)

    # upload splitted files
    for name in up_files:
        file_post(addr=arguments['data_server_addr'],
                  port=arguments['data_server_port'],
                  file_name=name)
        os.remove(name)
