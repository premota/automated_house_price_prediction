import os
import sys
from dataclasses import dataclass
import pandas as pd
import xgboost as xgb
from sklearn.metrics import r2_score

from src.logger import logging
from src.utils import save_object
from src.exception import CustomException

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_df, test_df):
        try:
            train_array = pd.read_csv(train_df)
            test_array = pd.read_csv(test_df)

            logging.info("split training and target features in test and train df")
            X_train, y_train, X_test, y_test = (
                train_array.iloc[:, :-1],
                train_array.iloc[:, -1],
                test_array.iloc[:, :-1],
                test_array.iloc[:,-1]
            )

            params = {
                'colsample_bytree': 0.6293177209695467,
                'gamma': 2.6931411837282537,
                'learning_rate': 0.8926154221799609,
                'max_depth': 3,
                'min_child_weight': 3,
                'subsample': 0.5179447928084266
                    }

            model = xgb.XGBRegressor(**params)

            # begin model training using custom hyper-parameter
            logging.info("model training using custom hyper-parameter")
            model.fit(X_train, y_train)

            #make predictions
            logging.info("make predictions and evaluate")
            y_pred = model.predict(X_test)

            #save trained model
            logging.info("save trained model as pickle file")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = model
            )

            # Evaluate the model on the test set using R2 score
            r2_test = r2_score(y_test, y_pred)
            print("R2 score on test set:", r2_test)

            return r2_test


        except Exception as e:
            raise CustomException(e, sys)
