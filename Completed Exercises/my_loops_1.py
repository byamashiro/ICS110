myname = input('What is your name? ')
myage = input('what is your age? ')
counter = 0


while counter < 10:
	print(myname)
	counter += 1

print('Part 1 complete.')

for age in range(1,int(myage)):
	print(age+1)

