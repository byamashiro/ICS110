myfname = 'bryan'
myage = 25
fname = input('Give your first name: ')

if myfname == fname:
	age = int(input('Give your age: '))
	if age == myage:
		print('Your identity has been verified!')
	else:
		print('Redo ages')
else:
	print('Wrong name!')