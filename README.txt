#ICS Python Notes

1: Basics and Installation
======================
--Setting up conda environment in a folder
Miniconda (https://conda.io/docs/install/quick.html)
--set up in command line 'bash Miniconda3-latest-MacOSX-x86_64.sh'
--be careful of path issues with stock python
	--if path is not set up, must use full path in home (/Users/bryanyamashiro/miniconda3/bin/)
	--test install by 'conda list' (full path)

--create virtual environment
mkdir classUH
cd classUH
conda create -n classUHenv python=3 #python=3.5
--if using python=integer, the latest version of the integer is used (can be specific)

--Activate and deactivate virtual environment
source activate classUHenv (full path)
source deactivate #deactivate classUHenv

--Installing additional packages
conda install ipython jupyter (full path)


--Creating alias in .bashrc in home directory
alias icsenv='cd /Users/bryanyamashiro/Desktop/ICS/classUH;source /Users/bryanyamashiro/miniconda3/bin/activate classUHenv'
-- The ';' allows to run a series of commands


2: Booleans, if/else
======================
!more newfile.txt
--in ipython, emulates vi command on command line


first = 'bryan'
last = 'yamashiro'

first + last
>> 'bryanyamashiro'

first + ' ' + last
>> 'bryan yamashiro'



run first_script.py
--runs python scripts in ipython

'py' * 5
>> 'pypypypypy'



--Running bash alias in ipython (~/.ipython/profile_default/ipython_config.py)
import re
import os.path

c = get_config()

with open(os.path.expanduser('~/.bashrc')) as bashrc:
    aliases = []
    for line in bashrc:
        if line.startswith('alias'):
            parts = re.match(r"""^alias (\w+)=(['"]?)(.+)\2$""", line.strip())
            if parts:
                source, _, target = parts.groups()
                aliases.append((source, target))

    c.AliasManager.user_aliases = aliases


3: Functions
==========
def print_stats():
    print('HP: 100')
    print('Mana: 50')
    print('Stamina: 35')
print_stats()


def attack(strength, weapon='sword'):
    print("Your strength is", strength, 'and you used a', weapon)
attack('high', 'dagger')
attack('low', weapon='spear')


def identify(weapon):
    if weapon == 'sword':
        return 'It attacks swiftly'
output = identify('sword')
print(output)

4: Loops
==========
--while loops
ipaddresses = 5
while ipaddresses <= 13:
    print('Scanning!', ipaddresses)
    ipaddresses = ipaddresses + 1 

while True: #with a break statement
-allows for a continuous loop until 'break'
while True:
    response = input('What would you like to do? ')
    if response == 'quit':
        break
    if response == 'q':
        break
print('You have quit')

-without a 'break' statement
response = input('What starter value do you want for response? ')
while response != 'quit':
    response = input('Sometimes this never shows: what new value for response do you want? ')
print('You have quit')

--for loops (creates a temporary variable)
for number in range(3):
    print(number)

total = 0
for pips in range(1, 7):
    total += pips                 # 1 + 2 + 3 + 4 + 5 + 6 --> 21
print('There are ' + str(total) + ' pips on a six-sided die')

-continue keyword
for num in range(20):
    if num % 3 == 1:
        continue
    print(num)


5: Strings
===========
---Attempt to use Bokeh over matplotlib (http://bokeh.pydata.org/en/latest/docs/gallery.html)
-Slider options
-Look up how to read in datetime elements from file
-Subplots relating to eachother
    -"Lined plots" example, "stocks"



--Specify strings with ''
var = 'string'
>>> string

--Raw strings
print(r'blah blah') #r before the ''


--Escape characters
\'   \"   \t   \n   \\


--Multiline strings
''' - triple quotes preserve natural new lines and leading spaces...

--Testing string characteristics
.isalpha(), .isalnum(), .isdecimal(), isspace(), .istitle(), .isupper(), .islower(), .startswith(), .endswith()

--String manipulation
.join(), .split(), .rjust(), .ljust(), .center(), .strip(), .rstrip(), .lstrip()

--String Formatting (https://pyformat.info)
positionals = '{1} {0}'.format('last', 'first')
name = '{first} {last}'.format(first='blah', last='bleh')


left_align = '{:20}'.format('blah') #alignment
left_align = '{:<20}'.format('blah')
right_align = '{:>20}'.format('blah')
center_align = '{:^20}'.format('blah')


6: Files
===========
--Writing to a file
fout = open('folder/output.txt', 'w')      # 'w' - write, 'r' - read
fout.write('''1
2
3''')
fout.close()

--Reading lines
* 'read()'                     # reads the file in as a single string
* 'readline()'                 # reads in one line at a time
* 'readlines()'                # reads in all lines, as separate strings in a list 
* 'for line in <filehandle>:'  # iterates over each line, one at a time

--Reading in patterns
data = open('folder/log_file.header.csv')
header = data.readline()
for line in data:
    if 'kara' in line:
        print(line)
    else:
        print('N/A')

data = open('folder/names.txt')
lineNum = 0
for line in data:
    lineNum += 1
    if line.startswith('S'):
        cleanline = line.rstrip() # Let's get rid of that pesky newline
        print(lineNum, cleanline)


--To download a .zip of the folder in Github (http://kinolien.github.io/gitzip/)


--Is there a way to look at a specific pattern in text files without reading in the remainder? (i.e 2011-08-09 in a year worth of data)

7: Lists
===========
--Why does the second for loop work, what is the syntax behind 'index,weapon'?
weapons = ['sword', 'axe', 'bow', 'dagger']

for index in range(len(weapons)):
    print('Weapon: ' + weapons[index] + '\t Indexed as ' + str(index))  
for index, weapon in enumerate(weapons):
    print('WEAPON: ' + weapon + '\t INDEXED as ' + str(index))



--why does assigning things to lists make them point to a value of None?
items ['a', 'b', 'c']
items = items.sort()
>> items = items


--The difference between list.append()  and list.extend(), append adds a single element.

blah = ['a', 'b', 'c']
print(blah[0])
>>> a

---Can load nested lists (listception)
microbe = [['bacteria', 'archaea', 'fungi', 'protists'], 
           ['single-celled', 'multicellular'],
           ['0.3 μm', '0.6 μm', '1.5 μm', '4 μm', '60 μm', '500 μm']]
microbe[1][1]
>> multicellular

--Slices (elements of list up to a certain index)
blah[0:2]
>> ['a', 'b']

overwrite an element in a list
blah[1] = 'a'
>> ['a', 'a']

--List manipulation
-concatenating lists
[1, 2, 3] + ['x', 'y', 'z']

for number in [10, 20, 30, 40]:
    print(number)
>> 10 \n 20 \n 30 \n 40

--list methods
.append(), .clear(), .copy(), .extend(), .index(), .insert(), .pop(), .remove(), .reverse(), .sort()

--Sorting key (changes sorting order)
junk = ['a', 'b', 'C', 'd', 'E']
junk.sort()
print(junk)
>> ['C', 'E', 'a', 'b', 'd']

junk = ['Z', 'b', 'C', 'd', 'E']
junk.sort(key=str.lower)
print(junk)
>> ['b', 'C', 'd', 'E', 'Z']

--Lists from delimited strings
del_string = 'bruce,selina,kara,clark,diana'
heroes = del_string.split(',')
print(heroes)
>> ['bruce', 'selina', 'kara', 'clark', 'diana']


aliases = 'batman superman aquaman robin catwoman'
my_heroes = aliases.split(' ')
print(my_heroes)
>> ['batman', 'superman', 'aquaman', 'robin', 'catwoman']

aliases2 = 'catwoman\nrobin     aquaman\tsuperman batman'
my_heroes = aliases2.split()      # Default is to split on whitespace
                                  # \n
                                  # \t
                                  # <space> or <spaces>
print(my_heroes)
>> ['catwoman', 'robin', 'aquaman', 'superman', 'batman']





