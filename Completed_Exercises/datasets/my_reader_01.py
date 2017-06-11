import pprint
import sys
from operator import itemgetter, attrgetter

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


print('The different characters: ',non_chars)

print('='*70)
count_x = 0
for line in data_r2:
	if line.startswith('x'):
		count_x += 1

print('Words starting with "x": ', count_x)

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
	if v_no == vowel_max:
		vowel_max_counter += 1


print(
'2 or more vowels: ', vowel_counter_2, '\n',
'3 or more vowels: ', vowel_counter_3, '\n',
'4 or more vowels: ', vowel_counter_4, '\n',
'5 or more vowels: ', vowel_counter_5, '\n',
f'Maximum Vowels with {vowel_max} characters: ', vowel_max_counter, '\n',
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

#print(vowels('bbbbb'))
data_r2_test = ['cacacaca', 'acacaca', 'caciceckcl']

#cv_dict = {}
counter_cv = {}

for line in data_r2:
	bool_con = 0
	bool_vow = 0

	cv_pattern = list(line)
	#print(line)
	con_counter = 0
	vow_counter = 0


#########consonants
	for i in cv_pattern[::2]:
		bool_c, count_c = vowels(i)
		con_counter += count_c
	if con_counter == 0:
		bool_con = 1
	else:
		bool_con = 0

#########vowels
	for j in cv_pattern[1::2]:
		bool_v, count_v = vowels(j)
		vow_counter += count_v
	if vow_counter == len(cv_pattern[1::2]):
		bool_vow = 1
	else:
		bool_vow = 0

	if line in counter_cv.keys():
		counter_cv[line] += 0
	else:
		counter_cv[line] = (bool_con + bool_vow)
		
	#print(bool_con + bool_vow)

##########Read into a dictionary
'''
for line in data:
	if line in counter_cv.keys():
		counter_cv[line] +=1
	else:
		counter_cv[line] = 1
'''
#print(counter_cv)
#sys.exit()
cv_chars = []

for line in counter_cv.keys():
	if counter_cv[line] == 2:
		cv_lines = line
		cv_chars.append(cv_lines)
		#print('working...')
	else:
		continue


print('Total amount of C-V words: ', len(cv_chars))
#print(cv_chars)


cv_max = 0
cv_max_counter = 0
for line in cv_chars:
	#boolean, v_no = vowels(line)
	if (len(line)) > cv_max:
		cv_max = (len(line))

for line in data_r2:
	if len(line) == cv_max:
		cv_max_counter += 1

print(f'Total number of {cv_max} character C-V words is: ', cv_max_counter)

print('=' * 70)


alpha_dict = {}
for item in data_r2:
	alpha_list = list(item)
	for i in alpha_list:
		alpha_dict[i] = alpha_dict.setdefault(i, 0) + 1

alpha_low = list(sorted(alpha_dict.items(), key=itemgetter(1)))
alpha_high = list(sorted(alpha_dict.items(), key=itemgetter(1), reverse=True))

print('The three letters that appear least frequently: ',alpha_low[:3])
print('The three letters that appear most frequently: ',alpha_high[:3])


data_r2_double = ['abaabess', 'abelsess', 'ssaesdffssfweffdsaa', 'sdfsdfa']
true_counter = 0
iterable = 0
double_dict = {}
for item in data_r2:
	double_list = list(item)
	iterable = 0
	true_counter = 0
	for i in double_list:
		iterable +=1
		#print(iterable)
		#print(i, ' ', double_list[iterable])
		try:
			if i == double_list[iterable]:
				letter1 = i
				letter2 = double_list[iterable]
				sequence_letter = letter1+letter2
				if sequence_letter in double_dict.keys():
					double_dict[sequence_letter] += 1
				else:
					double_dict[sequence_letter] = 1

				#print(word1+word2)
				#print(word1, ' ', word2)
				#print(double_list[iterable::1])
				#true_counter += 1
				#print(i, ' ', double_list[iterable])
				#for j in double_list:
				#double_dict[i] = double_dict.setdefault((word1+word2)) + 1

		except IndexError:
			pass
		#print(word1, ' ', word2)
#for j in double_dict:
#double_dict[j] = double_dict.setdefault((word1+word2), 0) + 1

high_double = sorted(double_dict.items(), key=itemgetter(1), reverse=True)

print('The letter that occurs most frequently as a double: ', high_double[:1])
'''
	for i in double_list:
		first = i
	if i == first:
		true_counter += 1
	#for j in double_list[1::1]:
	#	print('next: ', j)
	 	#if i == i[::2]:
	 	#	true_counter += 1
	 	#	print(i, ' ', i[::2])
	 	#alpha_dict[i] = alpha_dict.setdefault(i, 0) + 1
	print(true_counter)
'''

#pprint.pprint(alpha_dict)


#print(counter_cv)
'''
	if con_counter == len(cv_pattern[::2]):
		bool_con = False
	elif con_counter != len(cv_pattern[::2]):
	 	bool_con = False
	 		#elif con_counter == len(cv_pattern[::2]):
	#	bool_con = 2
	 		#print(con_counter)
	 	#print(cv_pattern[::2])
	 	#print(con_counter)
	 	#print(len(cv_pattern))
'''






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


	