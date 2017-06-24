import pandas as pd
from pandas import Series

bacteria_lengths = Series(range(1,5001,100), name='length')

#print(bacteria_lengths)
print(bacteria_lengths[23])
print(bacteria_lengths[23:27])

'''
logs = pd.read_csv('/Users/bryanyamashiro/Documents/ICS110/Completed_Exercises/15/pandas_numpy/log_file_1000.csv', names=['name',
                                                     'email',
                                                     'fm_ip',
                                                     'to_ip',
                                                     'date_time',
                                                     'lat',
                                                     'long',
                                                     'payload_size'])
'''