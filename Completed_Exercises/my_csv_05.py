import csv

def day(date):
	print(date)
	return date.split('/')[1]

'''
def day(date):
	date = date.split('/')
	date = date[0]
	return date

'''
fin = open('folder/yahoo_prices_short.csv')
header = fin.readline()

data = csv.reader(fin)

highest_vol = 0

for line in data:
	volume = int(line[5])
	dater = day(line[0])
	if volume > highest_vol:
		highest_vol = volume
		high_day = dater

print(high_day, highest_vol)