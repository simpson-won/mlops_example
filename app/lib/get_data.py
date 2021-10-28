import requests
import pandas as pd
from io import StringIO
import os

from app.lib.panda_util import split_data


#down_url="http://192.168.0.34:8091/files/"
#up_url = "http://192.168.0.34:8091/upload"
down_url="http://127.0.0.1:25478/files/"
up_url = "http://127.0.0.1:25478/upload"
params={'token':'f9403fc5f537b4ab332d'}

up_files = ['skl_train.csv', 'skl_test.csv']

all_data_file_name = 'skl_test_data.csv'


def file_post(file_name:str):
    """
    post file to file server

    param file_name, str
    """
    handle = open(file_name, 'rb')
    upload = {'file': handle}

    res = requests.post(url=up_url, params=params, files=upload)

    return res


def file_get(file_name:str):
    """
    get file from file server


    param file_name, str
    """
    down_url_1 = down_url + file_name
    r = requests.get(url=down_url_1, params=params)
    df = pd.read_csv(StringIO(r.text))

    return df


if __name__=="__main__":

    df = file_get(all_data_file_name)

    df_train, df_test = split_data(df, 0.33)

    df_train.to_csv(up_files[0])
    df_test.to_csv(up_files[1])

    # upload splitted files
    for name in up_files:
        file_post(name)
        os.remove(name)
