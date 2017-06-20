import re

#identify how many words start with an 'x'

with open('113809of.fic').readlines() as fin
pattern_x = re.compile(r'^[x]+$')
counter = 0

for lines in fin:
	word = lines.strip()
	matchobj = pattern_x.search(word)
	

