#import modules
import re


def vowels(word):
	count_v = 0
	lister = list(word)
	for i in lister:
		if 'a' in i:
			count_v += 1
		'''
		elif 'e' in i:
			count_v += 1
		elif 'i' in i:
			count_v += 1
		elif 'o' in i:
			count_v += 1
		elif 'u' in i:
			count_v += 1
		'''
	return True, count_v


# open and read the file
fin = open('113809of.fic').readlines()

# compile a pattern
pattern = re.compile(r'([a]*[a])+$', re.DOTALL) #^([^aeiouyAEIOUY0-9\W]+)$|^([aeiouyAEIOUY]+)$
counter = 0

# iterate over the words
for line in fin:
	word = line.strip()
	a_count = 0
	if 'e' not in word:
		for i in word:
			if 'a' in i:
				a_count += 1
		if a_count == 2:
			print(line.strip())
			counter += 1

print(f'There are {counter} words that match the criterion')


'''
	#print(word)
	#if len(word) % 2 == 0:
	if 'e' in word:
		#print(word)
		matchobj = pattern.search(word)
		if matchobj != None:
			print(matchobj)
			counter += 1
'''

# compare the word to pattern

#increment my counter

# present result