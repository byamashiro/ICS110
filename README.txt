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

--Customizing character class patterns
[0-9] matches any single numeric character
[0-9][0-9] matches any two numeric characters
[0-9][0-9][a-z] matches any two numeric characters followed by one lowercase alpha character
[0-9]{3} matches any three numeric character
[0-9]{2,8} matches any two to eight numeric characters
[a-zA-Z] matches any lowercase OR uppercase alpha character
[a-zA-Z_.#] matches any lowercase OR uppercase alpha character OR underscore OR literal period or hashtag
-i.e [A-Z@&*] for: contains a character class for uppercase letters AND these symbols: @, &, *

--when using regex command, does it repeat at the pointer, or at next iteration?
haRegex = re.compile(r'(ha){3}')
-i.e if the line was 'eeeeeeeeeee', would it start at index 0->1->2 or from first 'ee' to second 'ee'?
-regex completes things in a 'non-overlapping' style


--can you create nested capture groups?
-email = re.compile(r'(\S*)@(\D*.(\D*))')
-yes, the largest group is listed first, followed by the nested lists




11:  Internet
================================
--Reading in textfiles from online sources
import urllib.request
file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #data is read in as bytes
for line in file:
    print(line.decode().strip()) # converts bytes to strings using the .decode() attribute
>> But soft what light through yonder window breaks
>> It is the east and Juliet is the sun
>> Arise fair sun and kill the envious moon
>> Who is already sick and pale with grief


import pprint
import urllib.request
file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = {}

for line in file:
    words = line.decode().strip().split() #converts into a string > strip whitespace chars on string > list
    
    for word in words:
        # If a key for the word already exists .get() grabs the value otherwise it automatically returns 0
        count[word] = count.get(word, 0) + 1
pprint.pprint(count)

--HTML text
page = urllib.request.urlopen('http://dr-chuck.com/page1.htm')

for line in page:
    print(line.decode().strip())

>> <h1>The First Page</h1>
>> <p>
>> If you like, you can switch to the
>> <a href="http://www.dr-chuck.com/page2.htm">
>> Second Page</a>.
>> </p>

--Beautiful soup (conda install beautifulsoup4) [https://www.crummy.com/software/BeautifulSoup/bs4/doc/]
-Makes reading and parsing web pages a lot easier
-Allows you to extract tags of only certain types
-You can find certain tags based on their relationship in the tag heirarchy
-Getting hyperlinks becomes a whole lot easier

from bs4 import BeautifulSoup
import urllib.request
htmlText = urllib.request.urlopen('http://www.unicode.org/').read() #read method used in urllib...
soup = BeautifulSoup(htmlText, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

--Standing up a local HTTP server
$ cd path/to/the/lesson 11/folder/11
$ python -m http.server 8000

-able to run internet commands through localhost:8000
import urllib.request

file = urllib.request.urlopen('http://localhost:8000/annabel_lee.txt')
for line in file:
    print(line.decode().strip())

page = urllib.request.urlopen('http://localhost:8000/jabberwocky.html')
for line in page:
    print(line.decode().strip())

-is there a way to convert HTML to strings?


12, Part 1: JSON
====================================
--When executed (with eval or otherwise), this code creates and returns a JavaScript object which contains the data you serialized

import json

sample_zero = '''{
        "name":"merchandise",
        "properties":
        {
                "id":
                {
                        "type":"numeric",
                        "description":"merchandise identifier",
                        "required":true,
                        "format":"nn-nnn-nnnnnn"
                },
        }
}'''
info = json.loads(sample_zero)
print(type(info), info)

info['properties']['id']['format']
>> "nn-nnn-nnnnnn"

--json objects are mainly dictionaries with keys : values
-json objects are denoted with {}
-json arrays are denoted with []


--Example with .json
{"NKO": ["13.53", "13.52", "13.55"...

import json

with open('data.json') as inputfile:
    data = json.load(inputfile)

if '13.37' in data['NVY']:
    i = data['NVY'].index('13.37')
    print(i, data['NVY'][i])


--Example with .csv
exchange    stock_symbol    date    stock_price_open    stock_price_high    stock_price_low stock_price_close   stock_volume    stock_price_adj_close
AMEX    NKO 2/8/10  13.53   13.53   13.4    13.5    4500    13.5
AMEX    NKO 2/5/10  13.52   13.52   13.45   13.45   7500    13.45
AMEX    NKO 2/4/10  13.44   13.55   13.32   13.55   15800   13.55

import csv
import json

#with open('AMEX_daily_prices_N.csv', encoding='utf-8-sig') as fin:
with open('AMEX_daily_prices_N.csv') as fin:
    reader = csv.reader(fin)

    data = {}

    header = ''
    for line in reader:
        if not header:
            header = line
            continue
        exchange, stock_sym, date, _open, high, low, close, volume, adj = line
        #if stock_sym in ["NGX", "NKX", "NOX", "NVX", "NXE", "NXG", "NXI", "NXJ", "NXK", "NXM", "NXZ", "NZX"]:
        if 'X' in stock_sym:
            data[stock_sym] = data.get(stock_sym, []) + [close]

with open('x_stocks_test.json', 'w') as fout:
    json.dump(data, fout,
              indent=4,
              sort_keys=True)



12, Part 2: XML
==============================
--XML is a markup language similar to HTML in format but used to create fully customized markups. You can create elements using tags.

--sets - non-overlapping
s = set()
t = set([3, 4, 5, 6, 7, 8, 9])

s.update([1, 2, 3, 4, 5, 4, 4, 4, 4, 4]) # extra 4's will be neglected
print(s)
>> {1, 2, 3, 4, 5}

s.intersection(t) # values shared by s and t
>> {3, 4, 5}

s.difference(t) # values of t not in s
>> {1, 2}
t.difference(s)
>> {6, 7, 8, 9}

s.union(t) #shows full values of both
>> {1, 2, 3, 4, 5, 6, 7, 8, 9}



--set() vs. list vs. tuple

import xml.etree.ElementTree as ET

with open('catalog.xml', 'rb') as data:
    xmlParsed = ET.parse(data)

--Unique list of tags
elemList = set()
for elem in xmlParsed.iter():   # The iter() function can iterate over all the tags...
    elemList.add(elem.tag)      # sets automatically dedupe
print(elemList)


--Iterating over tags
for title in titles:
    print(title.get('id'))
titles = xmlParsed.iterfind('book/title')
for title in titles:
    print(title.text)

authors = xmlParsed.findall('book/author')
for name in authors:
    name = name.text
    fname, lname = name.split(', ')
    if len(lname) == 3:
        print(name)

--Writing to files
for elem in xmlParsed.iter('price'):
    price = float(elem.text)
    new_price = price + 100.0
    elem.text = str(new_price)
    
xmlParsed.write('output.xml')



13: Object Oriented Programming
========================================
--Class
A class is a type of template for the Python object. It lets Python know exactly what attributes and methods any object created from that class should have. It also provides instructions on what to do when creating OR destroying any given object

--Instance
An instance of a Python class is a singular Python object created using the template of a class that holds values or data that is unique to that instance. When methods are run they typically only change values inside a singular instance

--Attributes
Any given object has some attributes associated with it. These are values / data stored within the Python object that are tied to that specific object. You can access and use this data. Often some or all of the data associated with attributes is defined at the time an object is created, but this is not required and often values can be changed when needed.

--Methods
Any given object has methods associated with it. When creating a Python object the class will define the object's methods. These are functions tied to an instance. When you run a method it typically uses the attribute data as well as some data you give it to do one of a couple things:
-Change what the data inside the attributes are
-Return data from the attribute values
-Return data about the attributes of that object

--Object lifecycle
class Student:
    grade = 100
    
    def __init__(self):
        self.age = age
        print('I am created at the age of', self.age)
    
    def party(self):
        self.grade -= 10
        print('I partied so hard my grade is:', self.grade)

karen = Student(42)  # We only give it one parameter
print(karen.age)  # Note how age is what we gave it
>> 42

karen.party()
>> I partied so hard my grade is: 90

--Inheritance
class Student:
    grade = 100
    
    def __init__(self, age):
        self.age = age
        print('I am created at the age of', self.age)
    
    def party(self):
        self.grade -= 10
        print('I partied so hard my grade is:', self.grade)

class good_Student(Student):
    
    def study(self):
        self.grade += 10
        print('I worked hard and studied to bring my grade up to:', self.grade)

-parent class
steve = Student(15)

steve.party()
>> I am created at the age of 15
>> I partied so hard my grade is: 90

steve.study() # Inheriting from a parent class DOES NOT change the parent class
>> AttributeError: 'Student' object has no attribute 'study'

-inherited class
ellen = good_Student(17)

ellen.party()
>> I am created at the age of 17
>> I partied so hard my grade is: 90

ellen.study()
>> I worked hard and studied to bring my grade up to: 100






14: SQL
============================
--imports and connection
import sqlite3
conn = sqlite3.connect('data.db') # must always close connection after completion (i.e conn.close())


--creation of a table
sql = '''CREATE TABLE customers (first name text,
                                 last name text,
                                 email text,
                                 age integer)'''

--run SQL code
conn.execute(sql) # will break if the table already exists


--inserting values
con.execute(INSERT INTO table_name VALUES (?,?,?,...),
            (cust_id, fname, lname,))


--cursor method (.cursor()) is associated with the connection (i.e 'conn')
cur = conn.cursor()   # Create the cursor


--obtain data from SQL
for row in cur.execute('SELECT * FROM customers'):  # '*' is the wildcard, multiple variables can be called (i.e email, age,...)    
    print(row) # print(cur.fetchall()) will return a Python list of matching items, stored as tuples


--Adding more data in table and updating
ins3 = 'INSERT INTO customers VALUES (?, ?, ?, ?, ?)'
cur.execute(ins3, (5, 'Kara', 'Zor-el', 'kzorel@krypton.org', 33))

--or--

cur.execute("""UPDATE customers 
               SET email='bgordon@gotham.com' 
               WHERE email LIKE 'bgordon%'
               """)

print(cur.execute('SELECT * FROM customers WHERE age = 33').fetchall()) 



--More SQL syntax
-WHERE
for row in cur.execute('SELECT email, age FROM customers WHERE age > 34'): # can use others <,>,=,...

-ORDER BY (can also use descending using DESC)
for a, e in cur.execute('''SELECT age, email 
                           FROM customers 
                           WHERE age > 34 
                           ORDER BY age DESC'''):


-DISTINCT
for row in cur.execute('SELECT DISTINCT age FROM customers'):


-COUNT
for row in cur.execute('''SELECT email, COUNT(age) AS count
                          FROM customers
                          GROUP BY age
                          HAVING age > 34'''):


-GROUP BY -> HAVING/LIMIT (the second two methods require and depend on the 'GROUP BY' method)
for row in cur.execute('''SELECT age, COUNT(age) AS count
                          FROM customers
                          GROUP BY age
                          LIMIT 2'''): or HAVING age > 34'''):

-DELETE FROM
cur.execute("DELETE FROM customers WHERE first_name='Hal'")

for row in cur.execute('SELECT * FROM customers'):
    print(row)


--SQL example using .csv file
import sqlite3

conn = sqlite3.connect('my_second_sql.db')

sql = '''CREATE TABLE stocks (symbol text, # creating the table
                                date date,
                                open_price float,
                                close float,
                                volume integer)'''

try:
    conn.execute(sql)
except:
    pass

fin = open('AMEX_daily_prices_N.csv')
header = fin.readline()

for line in fin:
    exchange, stock_symbol, date, stock_price_open, stock_price_high, stock_price_low, stock_price_close, stock_volume, stock_price_adj_close = line.strip().split(',')
    conn.execute('INSERT INTO stocks VALUES (?,?,?,?,?)',
                    (stock_symbol, date, stock_price_open, stock_price_close, stock_volume))
    
cur = conn.cursor()

for row in cur.execute('''SELECT symbol, open_price, close
                        FROM stocks
                        WHERE close > 925'''):
    print(row)

conn.close() # remember to close out or database will be locked on following run



15: Pandas Dataframes and Series
====================================
--pandas is one of the premier data analysis libraries in the Python ecosystem. It offers high-performance, easy-to-use data structures and data analysis tools enabling you to carry out your entire data analysis workflow.

--simple example of loading series
import pandas as pd
from pandas import Series

s = Series([33, 37, 27, 42])
s.name = 'Justice League ages'
s.index = ['bruce', 'selina', 'kara', 'clark']


--indexing pandas series and index manipulation
s1 = Series([37, 36, 10, 36],
            index=['hal', 'victor', 'diana', 'billy'],
            name='More Justice League ages')

s1['billy']
>> 36


s1[['billy', 'victor', 'hal']]
>> billy     36
>> victor    36
>> hal       37
>> Name: More Justice League ages, dtype: int64

s1['hal':'diana'] # s1[0:3] slice notation still works with string-base index
>> hal       37
>> victor    36
>> diana     10
>> Name: More Justice League ages, dtype: int64


s1['diana'] = 32 # changes content of 'diana' from 10 -> 32


s1[s1 >= 35] # rows can be filtered with comparison operators (==, <=, >=)

s1[['diana', 'billy']]*20 # changed both indices temporarily by * 20


'diana' in s1 # boolean
>> True

'lex' in s1
>> False


--Analyzing data
s1 = Series(range(10, 16), index=['a', 'b', 'c', 'd', 'e', 'f'])
s2 = Series(range(16, 22), index=['a', 'b', 'c', 'x', 'y', 'z'])

s3 = s1 + s2
s3
>> a    26.0
>> b    28.0
>> c    30.0
>> d     NaN
>> e     NaN
>> f     NaN
>> x     NaN
>> y     NaN
>> z     NaN
>> dtype: float64

s3.isnull()
>> a    False
>> b    False
>> c    False
>> d     True
>> e     True
>> f     True
>> x     True
>> y     True
>> z     True
>> dtype: bool

s3.dropna()
>> a    26.0
>> b    28.0
>> c    30.0
>> dtype: float64


s4 = Series([42, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6])
s4
>> 0     42
>> 1      1
>> 2      1
>> 3      1
>> 4      2
>> 5      2
>> 6      3
>> 7      3
>> 8      3
>> 9      3
>> 10     3
>> 11     3
>> 12     4
>> 13     5
>> 14     6
>> dtype: int64

s4.unique()
>> array([42,  1,  2,  3,  4,  5,  6])

s4.value_counts()
>> 3     6
>> 1     3
>> 2     2
>> 42    1
>> 6     1
>> 5     1
>> 4     1
>> dtype: int64

s4.max() # note that pandas has unique methods relative to python
>> 42


def transmogrifier(x):
    new_val = '- ' + str(x ** 3) + ' -'
    return new_val

s4.apply(transmogrifier)
>> 0     - 74088 -
>> 1         - 1 -
>> 2         - 1 -
>> 3         - 1 -
>> 4         - 8 -
>> 5         - 8 -
>> 6        - 27 -
>> 7        - 27 -
>> 8        - 27 -
>> 9        - 27 -
>> 10       - 27 -
>> 11       - 27 -
>> 12       - 64 -
>> 13      - 125 -
>> 14      - 216 -
>> dtype: object

--Pandas data frames
from pandas import DataFrame
data = {'hero': ['billy', 'billy', 'billy', 'selina', 'selina'],
        'date': ['Jan 10', 'Jan 11', 'Jan 12', 'Jan 10', 'Jan 11'],
        'emails': [111, 121, 93, 211, 210]}

df = DataFrame(data, columns=['date', 'hero', 'emails', 'instagrams']) # since 'instagrams' doesn't exist, column will be populated with "NaN"
>>      date    hero  emails instagrams
>> 0  Jan 10   billy     111        NaN
>> 1  Jan 11   billy     121        NaN
>> 2  Jan 12   billy      93        NaN
>> 3  Jan 10  selina     211        NaN
>> 4  Jan 11  selina     210        NaN


df.index = [1, 2, 3, 4, 5] # changes row indexing starting from 1 instead of 0

df.columns
>> Index(['date', 'hero', 'emails', 'instagrams'], dtype='object')


df['hero'] # df.hero also works
>> 1     billy
>> 2     billy
>> 3     billy
>> 4    selina
>> 5    selina
>> Name: hero, dtype: object

df.loc[3] # outputs the third option
>> date          Jan 12
>> hero           billy
>> emails            93
>> instagrams       NaN
>> Name: 3, dtype: object


df.loc[1:5:2] # rows by 2 from 1 through 5
>>      date    hero  emails instagrams
>> 1  Jan 10   billy     111        NaN
>> 3  Jan 12   billy      93        NaN
>> 5  Jan 11  selina     210        NaN


from pandas import Series
df.instagrams = 50
ins = Series([10, 20, 30], index=[1, 3, 5])
ins
>> 1    10
>> 3    20
>> 5    30
>> dtype: int64


df.instagrams
>> 1    50
>> 2    50
>> 3    50
>> 4    50
>> 5    50
>> Name: instagrams, dtype: int64


df.instagrams = ins # instead of neatly changing index 1,3,5 the other values are replaced with "NaN"
df
>>      date    hero  emails  instagrams
>> 1  Jan 10   billy     111        10.0
>> 2  Jan 11   billy     121         NaN
>> 3  Jan 12   billy      93        20.0
>> 4  Jan 10  selina     211         NaN
>> 5  Jan 11  selina     210        30.0


df['overworked'] = df['emails'] >= 120
df
>>      date    hero  emails  instagrams  overworked
>> 1  Jan 10   billy     111        10.0       False
>> 2  Jan 11   billy     121         NaN        True
>> 3  Jan 12   billy      93        20.0       False
>> 4  Jan 10  selina     211         NaN        True
>> 5  Jan 11  selina     210        30.0        True


df[df.date == 'Jan 10'] # dataframes are mutable: columns can be added at will
>>      date    hero  emails  instagrams  overworked
>> 1  Jan 10   billy     111        10.0       False
>> 4  Jan 10  selina     211         NaN        True


data = {'billy': {'Jan 10': 202, 'Jan 11': 220, 'Jan 12': 198},
        'selina': {'Jan 09': 246, 'Jan 10': 235, 'Jan 11': 243}}
df2 = DataFrame(data) # data frame using dictionaries with nested dictionaries
df2
>>         billy  selina
>> Jan 09    NaN   246.0
>> Jan 10  202.0   235.0
>> Jan 11  220.0   243.0
>> Jan 12  198.0     NaN

-Transpose a data frame (i.e rows <-> columns)
dft = df2.T
dft
>>         Jan 09  Jan 10  Jan 11  Jan 12
>> billy      NaN   202.0   220.0   198.0
>> selina   246.0   235.0   243.0     NaN


nums = Series(range(10, 16),
              index=['t', 'u', 'v', 'x', 'y', 'z'])
nums
>> t    10
>> u    11
>> v    12
>> x    13
>> y    14
>> z    15
>> dtype: int64

i = nums.index
i
>> Index(['t', 'u', 'v', 'x', 'y', 'z'], dtype='object')

i[4]
>> 'y'

i[2:4] # index from 2 but not including 4
>> Index(['v', 'x'], dtype='object')

i[::2] # 1st and every following 2 index
>> Index(['t', 'v', 'y'], dtype='object')

i[::3] # 1st and every following 3 index
>> Index(['t', 'x'], dtype='object')



-methods with pandas dataframes
logs.fm_ip.unique()
logs.name.value_counts()
logs.name.head(7) # prints sample data
g = logs.groupby(logs.fm_ip)
g.get_group('106.152.115.161').head(3)

logs.columns

tf = logs.fm_ip == logs.to_ip

logs[['fm_ip', 'to_ip']].head(12)



16: Pandas read and write
===============================
--csv module
import pandas as pd
from pandas import Series, DataFrame

# webdata = pd.read_clipboard() # from html table sample_table.html, copy table direct


named_cols = pd.read_csv('log_file.csv',
                         names=['name', 
                                'email', 
                                'fmip', 
                                'toip',
                                'datetime', 
                                'lat', 
                                'long', 
                                'payload'])


skipped_rows = pd.read_csv('log_file.csv', 
                           names=['name', 'email', 'fmip', 'toip',
                                  'datetime', 'lat', 'long', 'payload'],
                           skiprows=[1, 2, 3, 7, 9])  # skiprows=range(1,10,3)
                           
skipped_rows.fmip # looking at one column 'fmip'

-separator value in separated values
sep='|'

-quick view of top or bottom values
piped_data.tail(4) # bottom 4 values
piped_data.head(4) # top 4 values

-choose index for data frame
import pandas as pd
date_index = pd.read_csv('log_file.csv', 
                         names=['name', 'email', 'fmip', 'toip',
                                'datetime', 'lat', 'long', 'payload'],
                         index_col='datetime')


-finding rows based off of index
date_index.loc['2016-02-06T21:44:56':'2016-02-06T21:49:36']


-Checking for NaN status and converting the particular values to an pandas NaN flag might not be optimal when loading data. You can turn this process off.
na_filter=False


-specify na_values to represent na values
na_values=['', '9999']

na_values=['', '9999'],
keep_default_na=False


-specify how many rows pandas should read
nrows=7

-read data in chunk by chunk for memory allocation optimization
data = pd.read_csv('log_file.csv', 
                   names=['name', 'email', 'fmip', 
                          'toip', 'datetime', 'lat',
                          'long', 'payload'],
                   chunksize=3)

for chunk in data:
    print('\npre-processing')
    print('more pre-processing')
    print('even more pre-processing')
    print(chunk)
    print('post processing\n')


-functions to transform one or more columns
def dsplitter(address):
    userid, domain = address.split('@')
    return userid, domain

def date_only(datetime):
    return datetime.split('T')[0]


data = pd.read_csv('log_file.csv', 
                   names=['name', 'email', 'fmip',
                          'toip', 'datetime', 'lat',
                          'long', 'payload'],
                   converters={'email':dsplitter,
                               'datetime':date_only})


-use only certain columns in a data file that is read in 
data = pd.read_csv('log_file.csv', 
                   names=['name', 'email', 'fmip',
                          'toip', 'datetime', 'lat',
                          'long', 'payload'],
                   usecols=['email', 'fmip', 'toip'])


--SQL with pandas
-pandas can read sql databases easily

import sqlite3
conn = sqlite3.connect('log_file.sql')
cur = conn.cursor()

df = pd.read_sql("SELECT * FROM superheroes", conn) # superheroes is a table in sql db


df1 = pd.read_sql('''SELECT datetime, email, lat, long FROM superheroes
                          WHERE name LIKE "%wayne%"''', conn)


df2 = pd.read_sql('''SELECT datetime, email, lat, long
                     FROM superheroes
                     WHERE name LIKE "%wayne%"''',
                  conn,
                  index_col='datetime')


--writing to disk
df2.to_csv('class_out.csv',
           cols=['email', 'lat', 'long', 'name'],
           header=True, sep='|')




17: Pandas data handling
===============================
--Merging data
import pandas as pd
from pandas import DataFrame, Series

readers1 = pd.read_csv('reader_stats.csv')
readers2 = pd.read_csv('reader_stats_short.csv')


readerso = pd.merge(readers1, readers2, how='outer') # all and overlap
readersi = pd.merge(readers1, readers2, how='inner') # only overlap
readersl = pd.merge(readers1, readers2, how='left')  # left and overlap
readersr = pd.merge(readers1, readers2, how='right') # right and overlap


--key columns to create joins
-use the 'on' option to sort the data
dfa = DataFrame({'key':     ['bruce', 'bruce', 'diana', 'bruce', 'hal', 'diana', 'kara'],
                 'emails_left': [112, 111, 201, 109, 113, 203, 204]}) 

dfb = DataFrame({'key':        ['hal', 'bruce', 'selina', 'diana'],
                 'ages_right': [36, 37, 33, 34]})

dfl = pd.merge(dfa, dfb, on='key', how='left')
dfi = pd.merge(dfa, dfb, on='key', how='inner')


--concatenation
names1 = Series(['wayne', 'jordan'], index=[1, 2])
names2 = Series(['dinah', 'kent'], index=[4, 5])
names3 = Series(['rayner', 'gordon', 'grayson'], index=[6, 7, 8])

pd.concat([names1, names3, names2], axis=0)
>> 1      wayne
>> 2     jordan
>> 6     rayner
>> 7     gordon
>> 8    grayson
>> 4      dinah
>> 5       kent
>> dtype: object


names4 = pd.concat([names1, names3])
pd.concat([names1, names4], axis=1)
>>         0        1
>> 1   wayne    wayne
>> 2  jordan   jordan
>> 6     NaN   rayner
>> 7     NaN   gordon
>> 8     NaN  grayson


output = pd.concat([names1, names3, names3], keys=['rho', 'sigma', 'tau'])
output
>> rho    1      wayne
>>        2     jordan
>> sigma  6     rayner
>>        7     gordon
>>        8    grayson
>> tau    6     rayner
>>        7     gordon
>>        8    grayson
>> dtype: object


output = pd.concat([names1, names3, names3], axis=1, keys=['rho', 'sigma', 'tau'])
output
>>       rho    sigma      tau
>> 1   wayne      NaN      NaN
>> 2  jordan      NaN      NaN
>> 6     NaN   rayner   rayner
>> 7     NaN   gordon   gordon
>> 8     NaN  grayson  grayson




dfa = pd.DataFrame([[11, 21, 31, 41],
                 [13, 25, 32, 49],
                 [11, 21, 31, 41],
                 [11, 21, 31, 42]], columns=['iota', 'kappa', 'lambda', 'mu'])

dfb = pd.DataFrame([[55, 66, 77],
                 [53, 63, 73]], columns=['kappa', 'lambda', 'mu'])

print(dfa)
print(dfb)
>>    iota  kappa  lambda  mu
>> 0    11     21      31  41
>> 1    13     25      32  49
>> 2    11     21      31  41
>> 3    11     21      31  42
>>    kappa  lambda  mu
>> 0     55      66  77
>> 1     53      63  73



pd.concat([dfa, dfb], ignore_index=True) # does not order index like the above prints
>>    iota  kappa  lambda  mu
>> 0  11.0     21      31  41
>> 1  13.0     25      32  49
>> 2  11.0     21      31  41
>> 3  11.0     21      31  42
>> 4   NaN     55      66  77
>> 5   NaN     53      63  73




import numpy as np

df = DataFrame(np.arange(100, 115).reshape((3, 5)),
               index=pd.Index(['kara', 'dinah', 'selina'], name='justiceleague'),
               columns=pd.Index(['wed', 'thu', 'fri', 'sat', 'sun'], name='day'))
df
>> day            wed  thu  fri  sat  sun
>> justiceleague                         
>> kara           100  101  102  103  104
>> dinah          105  106  107  108  109
>> selina         110  111  112  113  114


df.unstack() # The default level to unstack is the innermost
>> day  justiceleague
>> wed  kara             100
>>      dinah            105
>>      selina           110
>> thu  kara             101
>>      dinah            106
>>      selina           111
>> fri  kara             102
>>      dinah            107
>>      selina           112
>> sat  kara             103
>>      dinah            108
>>      selina           113
>> sun  kara             104
>>      dinah            109
>>      selina           114
>> dtype: int64


s = df.unstack()
s['wed']['kara']
>> 100

--multi index
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index
>> MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
>>            labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
>>            names=['first', 'second'])

s = pd.Series(np.random.randn(8), index=index)
s
>> first  second
>> bar    one      -1.437069
>>        two      -1.005649
>> baz    one       0.093091
>>        two      -0.637180
>> foo    one       1.257936
>>        two      -0.786610
>> qux    one       0.917287
>>        two       0.532761
>> dtype: float64

s.unstack(1)
>> second       one       two
>> first                     
>> bar    -1.437069 -1.005649
>> baz     0.093091 -0.637180
>> foo     1.257936 -0.786610
>> qux     0.917287  0.532761


s.unstack(0)
>> first        bar       baz       foo       qux
>> second                                        
>> one    -1.437069  0.093091  1.257936  0.917287
>> two    -1.005649 -0.637180 -0.786610  0.532761

s.unstack('second') # NOTE: You can refer to the level to unstack by the name of the Index.
>> second       one       two
>> first                     
>> bar    -1.437069 -1.005649
>> baz     0.093091 -0.637180
>> foo     1.257936 -0.786610
>> qux     0.917287  0.532761


--pivot table
league = DataFrame([['2016-03-10T00:00:00', 'jordan', 221],
                    ['2016-03-10T00:00:00', 'wayne', 222],
                    ['2016-03-10T00:00:00', 'kyle', 345],
                    ['2016-03-11T00:00:00', 'jordan', 222],
                    ['2016-03-11T00:00:00', 'wayne', 223],
                    ['2016-03-11T00:00:00', 'kyle', 323],
                    ['2016-03-12T00:00:00', 'jordan', 201],
                    ['2016-03-12T00:00:00', 'wayne', 209],
                    ['2016-03-12T00:00:00', 'kyle', 340],
                    ['2016-03-13T00:00:00', 'jordan', 220],
                    ['2016-03-13T00:00:00', 'wayne', 223],
                    ['2016-03-13T00:00:00', 'kyle', 339],
                    ['2016-03-14T00:00:00', 'jordan', 201],
                    ['2016-03-14T00:00:00', 'wayne', 219],
                    ['2016-03-14T00:00:00', 'kyle', 345]],
                    columns=['timestamp', 'jleague', 'tweets'])

tweet_view = league.pivot('timestamp', 'jleague', 'tweets')
tweet_view
>> jleague              jordan  kyle  wayne
>> timestamp                               
>> 2016-03-10T00:00:00     221   345    222
>> 2016-03-11T00:00:00     222   323    223
>> 2016-03-12T00:00:00     201   340    209
>> 2016-03-13T00:00:00     220   339    223
>> 2016-03-14T00:00:00     201   345    219


league['fan_index'] = abs(np.random.randn(len(league)))
league
>>               timestamp jleague  tweets  fan_index
>> 0   2016-03-10T00:00:00  jordan     221   0.428804
>> 1   2016-03-10T00:00:00   wayne     222   0.424633
>> 2   2016-03-10T00:00:00    kyle     345   0.129457
>> 3   2016-03-11T00:00:00  jordan     222   0.737199
>> 4   2016-03-11T00:00:00   wayne     223   1.560835
>> 5   2016-03-11T00:00:00    kyle     323   0.474609
>> 6   2016-03-12T00:00:00  jordan     201   0.279182
>> 7   2016-03-12T00:00:00   wayne     209   0.915738
>> 8   2016-03-12T00:00:00    kyle     340   0.662283
>> 9   2016-03-13T00:00:00  jordan     220   0.777396
>> 10  2016-03-13T00:00:00   wayne     223   1.021849
>> 11  2016-03-13T00:00:00    kyle     339   1.173358
>> 12  2016-03-14T00:00:00  jordan     201   1.004975
>> 13  2016-03-14T00:00:00   wayne     219   0.397957
>> 14  2016-03-14T00:00:00    kyle     345   0.458432



tweet_view2 = league.pivot('timestamp', 'jleague')
tweet_view2
>>                     tweets            fan_index                    
>> jleague             jordan kyle wayne    jordan      kyle     wayne
>> timestamp                                                          
>> 2016-03-10T00:00:00    221  345   222  0.428804  0.129457  0.424633
>> 2016-03-11T00:00:00    222  323   223  0.737199  0.474609  1.560835
>> 2016-03-12T00:00:00    201  340   209  0.279182  0.662283  0.915738
>> 2016-03-13T00:00:00    220  339   223  0.777396  1.173358  1.021849
>> 2016-03-14T00:00:00    201  345   219  1.004975  0.458432  0.397957


tweet_view2['fan_index']


--removing duplicates and replacing values
dfd = dfa
dfd['zeta'] = [4, 1, 4, 1]
dfd
>>    iota  kappa  lambda  mu  zeta
>> 0    11     21      31  41     4
>> 1    13     25      32  49     1
>> 2    11     21      31  41     4
>> 3    11     21      31  42     1



dfd.duplicated()
>> 0    False
>> 1    False
>> 2     True
>> 3    False
>> dtype: bool


dfd.duplicated(['iota', 'kappa'])
>> 0    False
>> 1    False
>> 2     True
>> 3     True
>> dtype: bool


dfd.drop_duplicates()
>>   iota  kappa  lambda  mu  zeta
>>0    11     21      31  41     4
>>1    13     25      32  49     1
>>3    11     21      31  42     1



genders = {'selina kyle': '1',
           'bruce wayne': '0',
           'dinah lance': '1',
           'hal jordan': '0',
           'clark kent': '0',
           'barry allen': '0',
           'arthur curry': '0',
           'billy batson': '0',
           'barbara gordon': '1',
           'kara zor-el': '1',
           'john jones': '0',
           'diana prince': '1',
           'dick grayson': '0',
           'john jones': '0',
           'victor stone': '0',
           'ray palmer': '0',
           'john constantine': '0',
           'kyle rayner': '0',
           'wally west': '0'}


it = pd.read_csv('ig_tweets.csv')
it
>>              jleague  igs  tweets
>> 0       billy batson    7       6
>> 1     barbara GORDON    3       8
>> 2     barbara gordon    9       5
>> 3   john constantiNe    4       6
>> 4        dinah lance    7       7
>> 5        selina kyle    4       3
>> 6       diana prince    6       9
...


it['gender'] = it['jleague'].map(genders) # Uses a dictionary to map keys to values
it
>>              jleague  igs  tweets gender
>> 0       billy batson    7       6      0
>> 1     barbara GORDON    3       8    NaN
>> 2     barbara gordon    9       5      1
>> 3   john constantiNe    4       6    NaN
>> 4        dinah lance    7       7      1
>> 5        selina kyle    4       3      1
>> 6       diana prince    6       9      1



it['jleagueLower'] = it['jleague'].apply(str.lower)
it
>>              jleague  igs  tweets gender      jleagueLower
>> 0       billy batson    7       6      0      billy batson
>> 1     barbara GORDON    3       8    NaN    barbara gordon
>> 2     barbara gordon    9       5      1    barbara gordon
>> 3   john constantiNe    4       6    NaN  john constantine
>> 4        dinah lance    7       7      1       dinah lance
>> 5        selina kyle    4       3      1       selina kyle
>> 6       diana prince    6       9      1      diana prince



it['gender'] = it['jleagueLower'].map(genders)
it
>>              jleague  igs  tweets gender      jleagueLower
>> 0       billy batson    7       6      0      billy batson
>> 1     barbara GORDON    3       8      1    barbara gordon
>> 2     barbara gordon    9       5      1    barbara gordon
>> 3   john constantiNe    4       6      0  john constantine
>> 4        dinah lance    7       7      1       dinah lance
>> 5        selina kyle    4       3      1       selina kyle
>> 6       diana prince    6       9      1      diana prince



def gen_conv(name):
    gen = genders[name.lower()]
    if gen == '0':
        return 'm'
    elif gen == '1':
        return 'f'

it['gender'] = it['jleague'].apply(gen_conv) # using .apply allows for function use
it
>>              jleague  igs  tweets gender      jleagueLower
>> 0       billy batson    7       6      m      billy batson
>> 1     barbara GORDON    3       8      f    barbara gordon
>> 2     barbara gordon    9       5      f    barbara gordon
>> 3   john constantiNe    4       6      m  john constantine
>> 4        dinah lance    7       7      f       dinah lance
>> 5        selina kyle    4       3      f       selina kyle
>> 6       diana prince    6       9      f      diana prince


it.gender.replace(['f', 'm'], ['Female', 'Male']) # doesnt seem to work as planned
>>              jleague  igs  tweets gender      jleagueLower
>> 0       billy batson    7       6      m      billy batson
>> 1     barbara GORDON    3       8      f    barbara gordon
>> 2     barbara gordon    9       5      f    barbara gordon
>> 3   john constantiNe    4       6      m  john constantine
>> 4        dinah lance    7       7      f       dinah lance
>> 5        selina kyle    4       3      f       selina kyle
>> 6       diana prince    6       9      f      diana prince



--bins
msgs = it.tweets
bins = [2, 5, 9, 15]

categories = pd.cut(msgs, bins)
categories
>> 0      (5, 9]
>> 1      (5, 9]
>> 2      (2, 5]
>> 3      (5, 9]
>> 4      (5, 9]
>> 5      (2, 5]
>> 6      (5, 9]


pd.value_counts(categories)
>> (5, 9]     20
>> (9, 15]    17
>> (2, 5]     13
>> Name: tweets, dtype: int64


labels = ['few', 'medium', "aren't there bad guys to catch"]
it['workload'] = pd.cut(it.tweets, bins, labels=labels) # labels in place of bin, 'label' must be one less than len(bins)
it
>>                           workload  
>> 0                           medium  
>> 1                           medium  
>> 2                              few  
>> 3                           medium  
>> 4                           medium  
>> 5                              few  
>> 6                           medium  


-is there a way to optimize sql databases? isnt it just adding more data, never decreasing?











