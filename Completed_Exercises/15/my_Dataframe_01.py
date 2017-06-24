import pandas as pd
from pandas import Series

na_log = pd.read_csv('/Users/bryanyamashiro/Documents/ICS110/Completed_Exercises/15/pandas_numpy/log_file_na.csv', names=['name', 'email', 'fm_ip', 'to_ip', 'date_time', 'lat', 'long', 'payload_size'])

payload = Series(na_log['payload_size'])
min_payload = payload.min()
max_payload = payload.max()


print('Delta payload: ', (max_payload - min_payload))
