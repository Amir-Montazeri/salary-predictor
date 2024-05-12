def calc_frequency(df, column_name: str):
  enc_column = (df.groupby(column_name).size()) / len(df)
  return enc_column

from time import time
from threading import Event, Thread 
class setInterval:
  def __init__(self, action, interval):
    self.action = action
    self.interval = interval
    self.stopEvent = Event()
    thread = Thread(target=self.__setInterval)
    thread.start()

  def __setInterval(self):
    nextTime = time() + self.interval
    while not self.stopEvent.wait(nextTime-time()):
      nextTime += self.interval
      self.action()

  def cancel(self):
    self.stopEvent.set()

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