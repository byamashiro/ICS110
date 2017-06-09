import csv

def val(volume, high, low):
	volume = str(round(int(volume)/1000000,1)) + 'M'
	high = float(high)
	low = float(low)
	del_hl = (high - low)
	return volume, del_hl

fin = open('folder/yahoo_prices_short.csv')
header = fin.readline()

data = csv.reader(fin)

for line in data:
	date = line[0]
	vol, delta = val(line[5], line[2], line[3])
	print ('date/volume/delta: ', date,'/',vol,'/',round(delta,2))