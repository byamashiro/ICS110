import csv

def IPcheck(ipaddress):
	if ipaddress.startswith('75.'):
		return True

fin = open('folder/log_file_1000.csv')
log_file = csv.reader(fin)

for line in log_file:
	name = line[0]
	fromip = line[2]
	toip = line[3]
	if IPcheck(fromip) and IPcheck(toip) == True:
		print('name/fromip/toip: ', name,'/', fromip, '/', toip)