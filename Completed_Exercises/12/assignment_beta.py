import csv
import sys

fin = open('AMEX_daily_prices_N.csv')
header = fin.readline()

data = csv.reader(fin)

list_st_names = []
for i in data:
	list_st_names.append(i[1])

#print(list_st_names)
#sys.exit(0)

counter = {}

for item in list_st_names:
	if item in counter.keys():
		counter[item] +=1
	else:
		counter[item] = 1


#print(counter.keys())


#for i in counter.keys():
#	print(i)
#sys.exit(0)

sum_price = []

for i in counter.keys():
	print(i)
	#print(data)
	for line in data: #code stops running at this line
		print(line, 'i am doing something')
		exchange, stock_symbol, date, stock_price_open, stock_price_high, stock_price_low, stock_price_close, stock_volume, stock_price_adj_close = (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
		print(exchange)
	
		if stock_symbol == i:
			#print(stock_symbol, round((float(stock_price_open) - float(stock_price_close)),2))
			diff = round((float(stock_price_close) - float(stock_price_open)),2)
			sum_price.append(diff)

print(sum_price)
print(round((sum(sum_price)), 2))

	#vol, delta = val(line[5], line[2], line[3])
	#print(date, stock_price_open, stock_price_close)
	 