import pprint
import sys

fin = open('113809of.fic')

data = []
for i in fin:
	cleanline = i.rstrip() # Let's get rid of that pesky newline
	data.append(cleanline)

fin.close()

fin2 = open('113809of.rev.2.fic')

data_r2 = []
for j in fin2:
	cleanline_r2 = j.rstrip() # Let's get rid of that pesky newline
	data_r2.append(cleanline_r2)

fin2.close()

print('File 1: ', len(data), ' ', 'File 2: ', len(data_r2))
print('Difference between the two files: ', (len(data) - len(data_r2)))

counter = {}

for item in data:
	if item in counter.keys():
		counter[item] +=1
	else:
		counter[item] = 1


for item in data_r2:
	if item in counter.keys():
		counter[item] +=1
	else:
		counter[item] = 1

#print(counter)
#print(type(counter))
#print(counter.values())

non_chars = []

for line in counter.keys():
	if counter[line] != 2:
		non_lines = line
		non_chars.append(non_lines)
		#print('working...')
	else:
		continue


print(non_chars)

print('='*70)
count_x = 0
for line in data_r2:
	if line.startswith('x'):
		count_x += 1

print('Words starting with x: ', count_x)

def vowels(word):
	count_v = 0
	lister = list(word)
	for i in lister:
		if 'a' in i:
			count_v += 1
		elif 'e' in i:
			count_v += 1
		elif 'i' in i:
			count_v += 1
		elif 'o' in i:
			count_v += 1
		elif 'u' in i:
			count_v += 1
	return True, count_v

vowel_counter_2 = 0
vowel_counter_3 = 0
vowel_counter_4 = 0
vowel_counter_5 = 0
no_vowel = 0
vowel_max = 0
vowel_max_counter = 0

for line in data_r2:
	boolean, v_no = vowels(line)
	if v_no >= 2:
		vowel_counter_2 += 1
	if v_no >= 3:
		vowel_counter_3 += 1
	if v_no >= 4:
		vowel_counter_4 += 1
	if v_no >= 5:
		vowel_counter_5 += 1
	if v_no == 0:
		no_vowel += 1
	if v_no > vowel_max:
		vowel_max = v_no

for line in data_r2:
	boolean, v_no = vowels(line)
	if v_no == 10:
		vowel_max_counter += 1


print(
'2 or more vowels: ', vowel_counter_2, '\n',
'3 or more vowels: ', vowel_counter_3, '\n',
'4 or more vowels: ', vowel_counter_4, '\n',
'5 or more vowels: ', vowel_counter_5, '\n',
'Maximum Vowels: ', vowel_max_counter, '\n',
'No Vowels: ',no_vowel
)
print('=' * 70)

'''
def cvcheck(cv_word):
	if cv_word != 'a' or 'e' or 'i' or 'u':
		return True
	else:
		return False
'''

print(vowels('bbbbb'))

cv_counter = 0
for line in data_r2:
	cv_pattern = list(line)
	for i in cv_pattern[::2]:
		bool_c, count_c = vowels(i)
		count_c += count_c
		if count_c == len(cv_pattern):
			


'''
	con = '0'
	vow = '0'
	boolean_c, cv_c_no = vowels(line[::2])
	boolean_v, cv_v_no = vowels(line[1::2])

	if boolean_c == None:
		con = True
	elif boolean_v == True:
		vow = True
	elif con and vow == True:
		cv_counter += 1
print(cv_counter)

'''






'''
def vowels(word):
	count_v = 0
	for i in range(len(word)):
		if 'a' in word:
			count_v += 1
			return True, count_v
'''
#print(vowels('aaaeeeiiiooouuuusdfna;lsdnflandf;lawhofvhaw;onv;awv;anw;odfnao;'))


'''
	if 'e' in word:
		return True
	if 'i' in word:
		return True
	if 'o' in word:
		return True
	if 'u' in word:
		return True
	else:
		return False
'''


	