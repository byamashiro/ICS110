b_list = {'name': 'byama', 'food':'sushi','music':'queen'}
print(b_list)
print(b_list['music'])


print('=' * 60)
b_list_2 = {'name':'brya', 'age':25, 'favfood':['sushi','ahi'], 'favsong':['bohemian rhapsody','hooked on a feeling','bleh']}
print(b_list_2)
print(b_list_2['age'])
print(b_list_2['favfood'])
print(b_list_2['favsong'])

print('=' * 60)
for i in b_list_2.keys():
	print(i)

for j in b_list_2.values():
	print(j)

for k, l in b_list_2.items():
	print(k, ' : ', l)
