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



