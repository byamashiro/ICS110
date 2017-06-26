import pandas as pd


list_range = list(range(0,1000,2))

fin = pd.read_csv('log_file_sign.csv', sep='!',  skiprows=list_range,index_col = 'datetime',names=['name', 'email', 'fmip',
                                'toip', 'datetime', 'lat',
                                'long', 'payload'])
print(fin.loc['2016-01-29T22:27:34':'2016-01-28T22:34:28'])
