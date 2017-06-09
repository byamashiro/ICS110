import csv

def llconv(latitude,longitude):
	latitude = round(float(latitude),2)
	longitude = round(float(longitude),2)
	return latitude,longitude


#print(llconv(12.3434, 213.3434))

fin = open('folder/log_file_1000.csv')
data = csv.reader(fin)

for line in data:
	date = line[4]
	#lati = line[5]
	#longi = line[6]
	#latlong = llconv(lati, longi)
	lati, longi = llconv(line[5], line[6])

	print('date/lat/long: ', date,'/', lati,'/',longi)