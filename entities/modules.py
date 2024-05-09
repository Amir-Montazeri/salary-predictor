def calc_frequency(df, column_name: str):
  enc_column = (df.groupby(column_name).size()) / len(df)
  return enc_column

class FrequencyEncoder:
  # rewrite the function as a class
  def __init__(self) -> None:
    self.frequency_list = {}

  def fit(self, df):
    pass

  def fit_transform(self, df, column_list):
    # df_copy = df.copy()
    print(df)
    return df
  #   for column in column_list:
  #     self.frequency_list.update({column: calc_frequency(df, column)})
  #     df_copy[column] = df[column].apply(lambda x: self.frequency_list[column][x])
  #   return df_copy
  
  # def transform(self, df, column_list):
  #   df_copy = df.copy()
  #   for column in column_list:
  #     df_copy[column] = df[column].apply(lambda x: self.frequency_list[column][x])

  def get_params(self, deep = True):
    return self.frequency_list

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