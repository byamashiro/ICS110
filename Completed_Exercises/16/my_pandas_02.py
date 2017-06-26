import sqlite3
import pandas as pd

conn = sqlite3.connect('log_file.sql')

cur = conn.cursor()
df = pd.read_sql('''SELECT lat,long,datetime
					FROM superheroes
					WHERE name LIKE "%barry%"''', conn)

print(df[0:11])