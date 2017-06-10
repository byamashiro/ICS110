user = {}

for i in ['Name', 'Phone', 'City', 'State']:
	#user[i] = user.setdefault(str(i), input(f'Enter your {i}: '))
	user[i] = user.setdefault(str(i), input('Enter your {}: '.format(i)))


print(user)

#print(f'{user["Name"]} hello blah bleh')