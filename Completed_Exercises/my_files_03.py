data = open('folder/log_file_1000.csv')

counter = 0

for line in data:
	counter += 1
	#print(counter)

	if "SELINA" in line:
		line = line.strip()
		print(counter, line)