import pandas as pd
from pandas import Series

na_log = pd.read_csv('/Users/bryanyamashiro/Documents/ICS110/Completed_Exercises/15/pandas_numpy/log_file_na.csv', names=['name', 'email', 'fm_ip', 'to_ip', 'date_time', 'lat', 'long', 'payload_size'])


print(na_log[['lat','long']])

diff_na = Series((na_log['long']-na_log['lat']))
print(diff_na.round(0).unique())
