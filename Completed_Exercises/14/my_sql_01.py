import sqlite3
conn = sqlite3.connect('my_first_sql.db')

sql = '''CREATE TABLE stocks (symbol text,
								date date,
								open_price float,
								close float,
								volume integer)'''

try:
    conn.execute(sql)
except:
    pass

fin = open('AMEX_daily_prices_N.csv')
header = fin.readline()

for line in fin:
	exchange, stock_symbol, date, stock_price_open, stock_price_high, stock_price_low, stock_price_close, stock_volume, stock_price_adj_close = line.strip().split(',')
	conn.execute('INSERT INTO stocks VALUES (?,?,?,?,?)',
					(stock_symbol, date, stock_price_open, stock_price_close, stock_volume))
	
cur = conn.cursor()

for row in cur.execute('SELECT * FROM stocks'):
	print(row)

conn.close()

