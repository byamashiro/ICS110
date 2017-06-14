import re

test_one = 'this_address@email.net'
test_two = 'USERname@aol.org'
test_three = 'my_thing@com' #should there be a .com here?
test_four = 'domain.org'
test_five = 'words.42@website.ly'

list_test_str = ['test_one', 'test_two', 'test_three', 'test_four', 'test_five']
list_test = [test_one, test_two, test_three, test_four, test_five]

email_sav = []
for i in list_test:
	if '@' in i and '.' in i:
		email = re.compile(r'(\S*)@(\w*).(\w*)') #need to escape dot \. "\." [.]
		myobj = email.search(i)
		print('email list: ', myobj.group(), '<--------This is an email address')
		print('sep. parts: ', myobj.groups())
		email_sav.append(myobj.group())
	else:
		website = re.compile(r'(\w*).(\w*)')
		myobj2 = website.search(i)
		print('website: ', myobj2.group())
		print('sep. parts: ', myobj2.groups())

print('Full Email Contact: ', email_sav)
