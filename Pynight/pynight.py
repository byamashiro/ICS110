import numpy as np

print('Hello World!')

a = (10+2)*5
b = (5*10)+2

print(a-b)

print(type(2.0))

one = 100
two = 2
three = 3

six = one + two + three
print(six)

print((((3 < 4) and (4 is not 5)) and ((4 != 5) or (6 == (3 * 2)))) )



x = 2 ** (1 / 2.0)
y = 1 + (1 / 3.0)
y_diff = 0

print(x == y, x > y)
x_diff = x - y
print(x_diff)


#for num in range(0,999999):
#	item = np.sqrt(num)
#	if isinstance(item,int):
#		print(num)

fac = 0
#list_fac = 
for i in range(12):
	fac += i*i
print(fac)

print(1*2*3*4*5*6*7*8*9*10*11*12)


print("She said, \"You can't just run around quoting people at random.\"")


str_method = 'String methods'.lower().title()
print(str_method)


booz = 'Booz Allen Hamilton'.split()
first, second, third = booz
first = first.split()
second = second.split()
third = third.split()


'''
first[0] = first[0].lower()
first[1] = first[1].lower()

second[-1] = second[-1].upper()
second[-2] = second[-2].upper()

third[2] = ''
third[4] = ''

print(first, second, third)

'''
'''
import csv
with open('yohosong.txt') as fin:
	log = csv.reader(fin, delimiter=' ')
	for i in log:
		print(i)
'''


'''
counter=0
fin = open('machistory.txt')
for line in fin:
	counter += 1
print(counter)
'''

import csv
yoho = 0
with open('yoHoHistory.txt') as fin:
	log = csv.reader(fin, delimiter='-')
	for i in log:
		yoho += int(i[0])

print(yoho)


a = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetuer', 'adipiscing', 'elit.', 'Maecenas', 'porttitor', 'congue', 'massa.', 'Fusce', 'posuere,', 'magna', 'sed', 'pulvinar']
b = ['ultricies,', 'purus', 'lectus', 'malesuada', 'libero,', 'sit', 'amet', 'commodo', 'magna', 'eros', 'quis', 'urna.', 'Nunc', 'viverra', 'imperdiet', 'enim.', 'Fusce', 'est.']

print(list(set(a) & set(b)))

'''
counter = 0
counter_1 = 0
near = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est.'
for i in near:
	if (str(i) not ',') or (str(i) not ' ') or (str(i) not '.'):
		counter_1 +=1
		if (str(i) < 'a'):
			counter += 1
		elif (str(i) > 'g'):
			counter+=1

print(counter, counter_1, int((counter/counter_1)*100))

'''
'''
from operator import itemgetter, attrgetter

data = open('pwlist.txt')

alpha_dict = {}
for item in data:
	alpha_list = list(item)
	for i in alpha_list:
		alpha_dict[i] = alpha_dict.setdefault(i, 0) + 1
alpha_high = list(sorted(alpha_dict.items(), key=itemgetter(1), reverse=True))
print(alpha_high)
print( (2151220 + 1272673), (1027141 + 1272673))
'''

decks = list('!^f$@\"N.#&S4K5MXd')
decks.sort()
print(decks[13])

names = ['crazy_guy', 'Noob_kid', 'power_gamer', 'power_kid', 'crazy_gal', 'power_dude', 'power_junky', 'power_guy', 'Noob_user', 'awesome_dude', 'bad_kid', 'bad_junky', 'cool_dude', 'crazy_gamer', 'crazy_dude', 'crazy_user', 'cool_junky', 'power_gal', 'awesome_gamer', 'awesome_junky', 'bad_user', 'Noob_gamer', 'bad_gal', 'power_user', 'cool_kid', 'cool_gamer', 'l33t_gamer', 'bad_dude', 'Noob_gal', 'l33t_dude', 'cool_user', 'crazy_kid', 'cool_gal', 'Noob_dude']
scores = reversed([178, 93, 253, 225, 177, 22, 262, 270, 158, 290, 295, 146, 57, 175, 196, 297, 153, 4, 67, 284, 178, 30, 126, 77, 152, 290, 53, 205, 253, 224, 35, 286, 165, 24])

total = list(zip(names,scores))
print(total)
'''
import json

with open('delicious_dataset_links.json', encoding='utf-8-sig') as inputfile:
	data = json.load(inputfile)

	print(data)

if '13.37' in data['NVY']:
	i = data['NVY'].index('13.37')
	print(i, data['NVY'][i])

'''
from datetime import date

d0 = date(2004, 8, 17)
d1 = date(2015, 8, 28)
delta = d0 - d1
print(delta.days)
'''
even = 0
for i in range(10,1001):
	if i % 2 == 0:
		print(even)
'''
'''
import json

with open('delicious_dataset_links.json', encoding='utf-8') as inputfile: #, encoding='utf-8-sig'
	data = json.load(inputfile)

	print(data)
'''
'''
if '13.37' in data['NVY']:
	i = data['NVY'].index('13.37')
	print(i, data['NVY'][i])
'''

print(2.0 + 10.5 * 4.0 - 3.0 / 1.0)

yoho=[]
fin = open('yohosong.txt')
for i in fin:
	yoho = i.rstrip()
	yoho_1 = yoho.replace(',', '')
	yoho_2 = yoho_1.replace('.', '')
	print(yoho_2)
	#for i in yoho_2:






