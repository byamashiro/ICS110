import csv
import sys

fin = open('AMEX_daily_prices_N.csv')
header = fin.readline()
data = csv.reader(fin)

list_st_names = []
for i in data:
	list_st_names.append(i[1])

counter = {}

for item in list_st_names:
	if item in counter.keys():
		counter[item] +=1
	else:
		counter[item] = 1


for i in counter.keys():
	sum_price = []
	fin.seek(0)
	#print(i)
	for line in data:
		exchange, stock_symbol, date, stock_price_open, stock_price_high, stock_price_low, stock_price_close, stock_volume, stock_price_adj_close = (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
	
		if stock_symbol == str(i):
			diff = round((float(stock_price_close) - float(stock_price_open)),2)
			sum_price.append(diff)

	if round((sum(sum_price)), 2) < -40.0:
		print(i, ' : ', round((sum(sum_price)), 2))
	else:
		continue
		#print(i, 'does not have a difference less than -40: ', round((sum(sum_price)), 2))
	 