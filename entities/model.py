import pandas as pd
import numpy as np
# from modules import FrequencyEncoder
from pydantic import BaseModel
import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def calc_frequency(df, column_name: str):
  enc_column = (df.groupby(column_name).size()) / len(df)
  return enc_column

class FrequencyEncoder:
  def __init__(self) -> None:
    self.frequency_list = {}

  def fit(self, df):
    print('-----------------------------------------------')
    print('fit: ', df)
    print('-----------------------------------------------')

  def fit_transform(self, df, df2):
    print('-----------------------------------------------')
    df_copy = df.copy()
    for column in df_copy.columns:
      self.frequency_list.update({column: calc_frequency(df, column)})
      df_copy[column] = df[column].apply(lambda x: self.frequency_list[column][x])
    df_copy.columns = df.columns
    print('fit_transform: ', df_copy.columns)
    print('-----------------------------------------------')
    return df_copy
  
  def transform(self, df):
    print('-----------------------------------------------')
    print('transformer: ', df)
    print('-----------------------------------------------')
    df_copy = df.copy()
    for column in df_copy.columns:
      df_copy[column] = df[column].apply(lambda x: self.frequency_list[column][x])
    df_copy.columns = df.columns
    return df_copy

  def get_params(self, deep = True):
    return self.frequency_list
  
  def get_feature_names_out(self, col_list):
    calced_col_list = self.frequency_list.keys()
    return calced_col_list

from sklearn.preprocessing import OrdinalEncoder
# ---------------------------------------------------------------------------------------------------------------

df = pd.read_csv('salaries.csv')
# del
df_uniques = pd.read_csv('salaries_uniques.csv')
# no null variable!
independent_columns = ['work_year', 'experience_level', 'employment_type', 'job_title', 'employee_residence', 'remote_ratio', 'company_location', 'company_size']
X_solid = df.loc[:, independent_columns]
y = df.loc[:, 'salary_in_usd']

cols_for_frequency_encoding = ['job_title', 'employee_residence', 'company_location']
cols_for_label_encoding = ['experience_level']
cols_for_one_hot_encoding = ['company_size', 'employment_type']

# Frequency Encoder
frequency_encoder = FrequencyEncoder()

# Label Encoder
label_encoder_experience_level = OrdinalEncoder(categories=[['EN', 'EX', 'MI', 'SE']], handle_unknown='error')

# One-Hot Encoder
from sklearn.preprocessing import OneHotEncoder
onehot_encoder_company_size = OneHotEncoder(drop='first', handle_unknown='error')
onehot_encoder_employment_type = OneHotEncoder(handle_unknown='error')

# Column Transformer
from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
  ('frequency_enc', frequency_encoder, cols_for_frequency_encoding),
  ('experience_level_enc', label_encoder_experience_level, ['experience_level']),
  ('company_size_enc', onehot_encoder_company_size, ['company_size']),
  ('employment_type_enc', onehot_encoder_employment_type, ['employment_type'])
], remainder='passthrough', verbose_feature_names_out=True)
X = preprocessor.fit_transform(X_solid)
X = pd.DataFrame(X)
X.columns = preprocessor.get_feature_names_out()

# Stringifying columns to prepare data for feature scaling
# X.columns = X.columns.astype('str')

# # Split Test&Train
from sklearn.model_selection import train_test_split
X_train_solid, X_test_solid, y_train, y_test = train_test_split(X, y, test_size=0.1 , random_state=0, stratify=X['remainder__work_year'])

# Feature Scaler
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = pd.DataFrame(sc_x.fit_transform(X_train_solid))
X_test = pd.DataFrame(sc_x.transform(X_test_solid))

# Renaming the feature names as before
X_train.columns = X_train_solid.columns
X_test.columns = X_test_solid.columns

# Model (RandomForest)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)

def predictor(X_pred):
  processed_X_pred = pd.DataFrame(preprocessor.transform(pd.DataFrame(X_pred, index=[0])))
  processed_X_pred.columns = preprocessor.get_feature_names_out()
  y_predicted = regressor.predict(processed_X_pred)
  # rounded_y_predicted = round(y_predicted, 2)
  return y_predicted

def get_accuracy():
  accuracy = round(regressor.score(X_test, y_test) * 100, 2)
  return accuracy
print('accuracy: ', get_accuracy())

# class Model_Input(BaseModel):
#   work_year: int
#   experience_level: str
#   employment_type: str
#   job_title: str
#   employee_residence: str
#   remote_ratio: int
#   company_location: str
#   company_size: str

def get_unique_features():
  uniques = {}
  for col in X_solid.columns:
    uniques[col] = X_solid[col].unique()
  return uniques