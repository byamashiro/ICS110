user = {}

for i in ['Name', 'Phone', 'City', 'State']:
	user[i] = user.setdefault(str(i), input('Enter your {}: '.format(i)))

print(user)