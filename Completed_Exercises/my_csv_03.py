import csv

def stk(high,low):
	high = float(high)
	low = float(low)
	del_hl = (high - low)
	return del_hl

fin = open('folder/yahoo_prices_short.csv')
header = fin.readline()
data = csv.reader(fin)

for line in data:
	date = line[0]
	delta = stk(line[2], line[3])
	print('date/delta: ', date,'/',round(delta,1))