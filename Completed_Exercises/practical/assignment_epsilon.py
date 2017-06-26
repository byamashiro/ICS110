import sqlite3
import pandas as pd

conn = sqlite3.connect('log_file.sql')
cur = conn.cursor()

df = pd.read_sql('''SELECT name,payload,datetime
				FROM superheroes
				WHERE  payload > 48600 and payload < 489500
				''', conn)
#df.head()


print('Minimum payload value: ',df.payload.min())
print('Maximum payload value: ',df.payload.max())
print('Median payload value: ',df.payload.median())
print('='*30)

print(f'All payload values:\n{df.payload}')
print('='*30)
print(df.info())

#print()