import pandas as pd
import sys

fin = pd.read_csv('log_file_1000.csv', sep=',',names=['name', #'python',
													'email',
													'fmip',
													'toip',
													'datetime',
													'lat',
													'long',
													'payload_size']) #,  skiprows=list_range,index_col = 'datetime'
fin.index.name = 'python'
print(fin)
same_ip = fin[fin.fmip == fin.toip]
same_ip_len = len(same_ip)
#print(same_ip_len)

#sys.exit(0)

#print('A sample of similar rows include: ', same_ip)

print('Similar (to/fm) IP Rows: ', same_ip_len)



print('='*30)


unique_payload = fin.payload_size.unique()

#print(unique_payload)
print('Unique values in payload: ', len(unique_payload))

print('='*30)

#print(fin.fmip.value_counts())
print(f'The highest fmip, {fin.fmip.value_counts().index[0]}, occurs {fin.fmip.value_counts().max()} times')
print(f'The lowest fmip, {fin.fmip.value_counts(ascending=True).index[0]}, occurs {fin.fmip.value_counts().min()} times')

print('='*30)
'''
print('Value counts in fmip column: ', len(fin.fmip.value_counts()))
print('Highest count: ', fin.fmip.value_counts().max())
print('Lowest count: ', fin.fmip.value_counts().min())

print('='*30)
'''
for i in range(8):
	print(fin.columns.values[i])

print('='*30)
print('A sample of similar rows include: ', same_ip)
print('Unique values stored in payload: ' ,unique_payload)

