import pandas as pd


def split_data(df, test_ratio:float):
    """
    split data by test_ratio
    """
    data_size = len(df.index)
    test_size = int(data_size*test_ratio)
    train_size = data_size - test_size
    df_train = df.iloc[:train_size, :]
    df_test = df.iloc[train_size + 1:, :]
    return df_train, df_test


def get_X_y(data):
    X = data[data.columns[1:]]
    X = X[['Sex', 'Age_band', 'Pclass']]
    y = data['Survived']

    return X, y
