my_csv = open('folder/log_file_1000.csv')

for line in my_csv:
	if '220.211.18.31' in line:
		print(line)
	else:
		print('N/A')

my_csv.close()