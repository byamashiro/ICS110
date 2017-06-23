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



#print(i)
#fin.seek(0)

counter_cl_nib = 0
counter_op_nib = 0
counter_both_ib = 0
list_st_over = []

for i in counter.keys():
	sum_price = []
	fin.seek(1)
	header = fin.readline()
	counter_both_ib = 0

	for line in data:
		stock_symbol = line[1]
		stock_price_open = float(line[3])
		stock_price_close = float(line[6])
			#print(stock_symbol, stock_price_open, stock_price_close)
		if stock_symbol == str(i):
			if (stock_price_open > 30 and stock_price_open < 420) and (stock_price_close > 32 and stock_price_close < 422):
				#print('both sets of bounds', stock_symbol, stock_price_open, stock_price_close)
				counter_both_ib += 1
	if counter_both_ib > 0:
		list_st_over.append(i)
	#print(i, ' : ',counter_both_ib)
print(list_st_over)

with open("assignment_gamma_result.csv",'w') as resultFile:
	wr = csv.writer(resultFile, dialect='excel')
	#wr.writerow([list_st_over[0],list_st_over[1]]) #this will print it out on one line
	wr.writerow([list_st_over[0],list_st_over[1]])
	wr.writerow([list_st_over[2],list_st_over[3]])
	wr.writerow([list_st_over[4],list_st_over[5]])


'''
	if (stock_price_open > 32 and stock_price_open < 420) and not (stock_price_close > 32 and stock_price_close < 422):
		print('closing not in bounds: ', stock_symbol, stock_price_open, stock_price_close)
		counter_cl_nib += 1


	elif (stock_price_close > 32 and stock_price_close < 422) and not (stock_price_open > 32 and stock_price_open < 420):
		print('opening not in bounds: ', stock_symbol, stock_price_open, stock_price_close)
		counter_op_nib += 1
'''



#print(counter_cl_nib, counter_op_nib, counter_both_ib)





'''
		if stock_symbol == str(i):
			if stock_price_open > 32 and stock_price_open < 420:
				if stock_price_close > 32 and stock_price_close < 420:
				#print(stock_symbol, stock_price_open, stock_price_close)

				diff = round((float(stock_price_close) - float(stock_price_open)),2)
			sum_price.append(diff)
'''
#print(line)
'''
		if stock_price_open > 32 and stock_price_open < 420:
			if stock_price_close > 32 and stock_price_close < 420:
				print(stock_symbol, stock_price_open, stock_price_close)
'''
'''
		if stock_symbol == str(i):
			diff = round((float(stock_price_close) - float(stock_price_open)),2)
			sum_price.append(diff)

	if round((sum(sum_price)), 2) < -40.0:
		print(i, ' : ', round((sum(sum_price)), 2))
	else:
		continue
'''
		#print(i, 'does not have a difference less than -40: ', round((sum(sum_price)), 2))
	 