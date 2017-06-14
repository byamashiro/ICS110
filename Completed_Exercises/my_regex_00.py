import re

pattern = re.compile(r'\d\d-\d\d-\d\d')

matchObj = pattern.search('blah blah blah my number is 15-23-42')

print('your number is: ', matchObj.group())

#======part 1
print(('=' * 30) + 'Part 1' + ('=' * 30))
pattern1 = re.compile(r'(\d\d\d)-\d\d-\d(\d\d\d)')
myObj = pattern1.search('which number 23-222-3333 OR 234-33-4455 is an SSN?')

print('result is: ', myObj.group())
print('result is: ', myObj.group(0))
print('result is: ', myObj.group(1))
print('result is: ', myObj.groups())
print('result is: ', myObj.span())


#======part 2
print(('=' * 30) + 'Part 2' + ('=' * 30))

pattern2 = re.compile(r'(\w){3,5}')
matchObj2 = pattern2.search('Can you find &ME* or @YOU but not )WE')

matchObj3 = pattern2.findall('Can you find &ME* or @YOU but not )WE')
print('content: ', matchObj2.group(), matchObj3)