import sys

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class ModelingSkl:
    def __init__(self):
        pass

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2


    def run_modeling(self,
                     n_estimator,
                     train_X,
                     train_y,
                     test_X,
                     test_y):
        model = self._get_rf_model(n_estimator)

        model.fit(train_X, train_y)
        predicted_y = model.predict(test_X)
        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_y)

        model_info={
            'score':{
                'model_score':model.score(train_X, train_y)
            },
            'params':model.get_params()
        }

        predict_info={
            'rmse':rmse,
            'mae':mae,
            'r2':r2
        }

        print('model =\n', str(type(model)) + '\n', model)

        return model, model_info, predict_info

    def _get_rf_model(self, n_estimator):
        return RandomForestClassifier(n_estimators=n_estimator, max_depth=5)


