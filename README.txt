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

--Reading csv/tsv files
-csv example
import csv                          # The csv module provides more flexibility and tools than 
                                    # opening the file with straight Python
file = open('folder/stocks.csv')
file.readline()    
csv_stocks = csv.reader(file)       # produces a reader object that parses rows
                                    # the way you expect, out of the box
                                    #     defaults to comma separator
                                    #     understands quoted fields
open_prices = list()
for line in csv_stocks:
    symbol = line[0]
    name = line[1]
    high = line[3]
    
    open_prices.append(high)
    print(symbol, name, high)
print('\nMax:', max(open_prices))   # NOTICE the '\n' character
file.close()



-tsv example
import csv                          # The csv module provides more flexibility and tools than 
                                    # opening the file with straight Python
file = open('folder/stocks.tsv')
file.readline()                     # "Stock Symbol","Stock Name",Open,High,Low,Close,Volume,Adj Close
tsv_stocks = csv.reader(file, delimiter='\t', quotechar="'",escapechar="\\")                        
                                    # csv.reader takes several arguments here
                                    #     the filehandle
                                    #     a delimiter character 
                                    #     a quote character to encapsulate any 
                                    #     delimiters
                                    #     an escape character
open_prices = list()
for line in tsv_stocks:
    print(line)
    symbol, name, _open, high, low, close, volume, adjclose = line
    open_prices.append(high)
    print(symbol, name, high)
print('\nMax:', max(open_prices))
file.close()


--Dialect saving to save parameters (i.e What was defined as a delimiter)
# If you're going to read a bunch of CSVs with the same style of formatting then you can
# make a "dialect" which saves some of your arguments

file = open('folder/stocks.tsv')
csv.register_dialect('tsvDialect', delimiter='\t', quotechar="'", escapechar="\\")

tsvinput = csv.reader(file, 'tsvDialect')

for line in tsvinput:
    print(line)


--Use of functions and an if statement of an empty variable
import csv

def dayFromDate(date):
    return date.split('/')[1]
    
with open("folder/yahoo_prices_short.csv") as fin:
    fin.readline()                              # read in header
    logs = csv.reader(fin)
    
    highest_vol = 0
    
    for line in logs:
        date, _open, high, low, close, volume, adj_close = line # unpack full columns
        volume = int(volume)
        if volume > highest_vol:                # If the line has a higher volume, print the day of that line
            highest_vol = volume                # Replace the volume as highest if it is greater
            day = dayFromDate(date)
        
    print(day, highest_vol)




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

--Use the wildcard when unpacking 'king arthur' *stuff, can you average all of *stuff?

--PPrint
import pprint
pprint.pprint(object) #list (i.e Data)

mString = pprint.pformat(object)

8: Dictionaries
====================
--Initializing a dictionary, str/float/int/list all work within the dictionary
contact = {'name': 'Arthur', 'number': '867-5309', 'email': 'genericEmail@gmail.com'}



--Adding an element to the dictionary
contact['address'] = ['42-503 Lorelana Dr.', 'Honolulu HI', '95746']



--keys()-header, values()-values, items()-both header and values
contact.keys()
contact.values()
contact.items()

-able to iterate over a loop to see contents
for key in contact.keys(): #same with values()
    print(key)
>> name
   number
   email
   address
   account_status

-iterate to see both keys and values using 'items()'
for k, v in contact.items():
    print(k + ":\t", v)
>> name:    Arthur
   number:  867-5309
   email:   genericemail42@gmail.com
   address:         ['42-503 Lorelana Dr.', 'Honolulu HI', '95746']



--Alterting and checking if elements exist within a dictionary
-.get()
contact.get('account_status', 'No account recorded')
>> No account recorded
-WARNING: .get() does NOT alter OR update the dictionary.

-.setdefault(), Actually sets an object within the dictionary and alters current dictionary
contact.setdefault('account_status', 'No account')
-If the value already exists, it will read the current occupier, does not overwrite


--Use dictionaries to count
METHOD 1

mList = list('this is going to be a list for us to count which letter occurs most often')

count = {} # We create our counting dict

for item in mList:
    if item in count.keys():   # We check to see if we've already made a key for this item
        count[item] += 1       # Then we add one to the tally
    else:                      # If it hasn't shown up then we create a key for that item and set its value to 1
        count[item] = 1

count


METHOD 2

mList = list('this is going to be a list for us to count which letter occurs most often')
count = {}

for item in mList:
    count[item] = count.get(item, 0) + 1    # Using the get method we don't need to have a value there
                                            # already because if it isn't there it evaluates to 0
                                            # by default
count

-Why does 'count.setdefault(item,0)' work in this case?

--Pretty printing module
import pprint
pprint.pprint(contact)

-save as a variable
import pprint
text = pprint.pformat(contact)
print(text)


9: Tuples
=====================================
Tuples are very similar to lists however they're a lot simpler.
There is a reason for this... tuples are intended to be immutable

--Sample tuples
superhero = tuple(['bruce wayne', 'gotham', 'batman']) = ('bruce wayne', 'gotham', 'batman')
sample_tuple = ('diana', )
superhero[1]
>> gotham

--tuples vs. lists
name_d = ['bruce', 'wayne']
name_t = ('selina', 'kyle')
characters = {name_d: 'batman'}
>> TypeError: unhashable type: 'list'
characters = {name_t: 'catwoman'}
>> {('selina', 'kyle'): 'catwoman'}

--sorted() function
-what can be sorted by the sorted() function?
~Iterable-sequence (string, tuble, list) or collection (set, dictionary, frozen set) or any iterator

-what does the sorted() function return?
~a sorted list from the given iterable

-what does key allow you to do?
~function that serves as a key for the sort comparison

-what is the default setting for reverse?
~if True, the sorted list is reversed (default = False)

-what type of function is sorted()?
~a method that sorts the elements of a given list


--named tuples
Named tuples are a mechanism for creating tuples with: names,named attributes

from collections import namedtuple
Heroine = namedtuple('Heroine', ['fname', 'lname'])
heroine = Heroine('diana', 'prince')
type(heroine)
>> __main__.Heroine
heroine.lname
>> 'prince'
heroine.fname
>> 'diana'


h = 'baba'
h[::2]
>> 'bb'
h[1::2]
>> 'aa'


10: Regular Expressions
=====================================
--re.compile(r'string')
Sets the pattern that you want to observe

--re.search('string')
Searches for the expression defined in the compile statement - usually assign this to a label for result print

import re
phonePattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObj = phonePattern.search('My number is ###-###-####')
print('found numbers:', matchObj.group())

--break up/segregate matches into submatches using nested parenthesis
phonePattern2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
-this allows indexing for matches starting from [0]

--use the .span() to find the range of slices
matchObj.span()
'My number is ###-###-####'
 |    |       |          |
 0    5      13         24

 --use the .groups() to print all subgroups

 --use the (|) character for 'OR', to match multiple patterns
 multiRegex = re.compile(r'hat|cat')

--If you need to repeat a character OR string of characters OR a character class, you can tell the re module how many times to repeat using a number in {}
haRegex = re.compile(r'(ha){3}')
result = haRegex.search('hehahahahahehe').group()
print(result)
>> hahaha

--If we want to find any sequence between 3 and 5 units long: we can use a range-style notation
haRegex = re.compile(r'(ha){3,5}')
-To alter this behavior, you can tell the regex module to be lazy, using the '?' which will default to the shortest string that matches the pattern


--For those times when you want to find all instances of a pattern NOTE: findall returns a list NOT a matchObj
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.findall('Home: ###-###-####, Cell: ###-###-####')


Character class Represents
\d  :  numeric digits 0-9
\D  :  everything BUT digits 0-9
\w  :  any letter, numeric or underscore character
\W  :  everything BUT letters, numerics, or underscores
\s  :  spaces, tabs, and newline characters
\S  :  everything BUT spaces, tabs, and newlines


Regex symbols      Their function
?               :  matches zero or one (also drives lazy matching, see below
*               :  matches zero or more
+               :  matches one or more
{n}             :  matches exactly n
{n,}            :  matches n or more
{,m}            :  matches 0 to m
{n,m}           :  matches at least n and at most m
{n,m}?, *?, +?  :  performs a non-greedy(lazy) match
^spam           :  the string must begin with spam
spam$           :  the string must end with spam
.               :  matches any character except newlines
[abc]           :  matches any character between the brackets
[^abc]          :  matches any character but the ones between the brackets


mo = re.search(r'\d', 'A1B2C3')
mo.group()
re.findall(r'\d', 'A1B2C3')
>>  ['1', '2', '3']

--Flags
re.IGNORECASE (or re.I), re.DOTALL, re.VERBOSE

-helloRegex = re.compile(r'hello', re.IGNORECASE)
print(helloRegex.findall('I said "HELLO!" to the man after he said hello to me'))
>> ['HELLO', 'hello']

-dotallRegex = re.compile(r'.*') - this stops at the new line dot (.) will match all characters except a newline, (*) will repeat the previous pattern multiple times
dotallRegex = re.compile(r'.*', re.DOTALL)
print(dotallRegex.search('Batman is love\nBatman is life').group())
>> Batman is love (first line stops here)
>> Batman is life

-phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
VERSUS...
phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?
                            (\s|-|\.)?          # space OR hyphen OR literal dot (lazy)
                            \d{3}
                            (\s|-|\.)           # space OR hyphen OR literal dot 
                            \d{4}
                            (\s*(ext|x|ext.)\s*\d{2,5})?     # variations on extensions
                            )''', re.VERBOSE)
-allows for clean commenting 

-possible to combine flags using (|)
re.compile(r'example string', re.VERBOSE | re.IGNORECASE)



--when using regex command, does it repeat at the pointer, or at next iteration?
haRegex = re.compile(r'(ha){3}')
-i.e if the line was 'eeeeeeeeeee', would it start at index 0->1->2 or from first 'ee' to second 'ee'?

--can you create nested capture groups?
-email = re.compile(r'(\S*)@(\D*.(\D*))')













