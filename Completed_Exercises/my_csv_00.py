import csv

def getUID(email):
	return email.split("@")[0]

#print(getUID('blah@bleh.edu'))

fin = open('folder/log_file_1000.csv')

data = csv.reader(fin)

#finder = list[]

for line in data:
	name = getUID(line[1])
	latitude = line[5]
	longitude =line [6]
	print('name/latitude/longitude: ', name,'/',latitude,'/',longitude)