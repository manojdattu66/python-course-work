Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name:'Venky is good boy'
name.upper()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name.upper()
NameError: name 'name' is not defined
name='Venky is good boy'
name.upper()
SyntaxError: multiple statements found while compiling a single statement
name='Venky is good boy'
name.upper()
'VENKY IS GOOD BOY'
name='Venky is good boy'
name.lower()
'venky is good boy'
name='Venky is good boy'
name.capitalize()
'Venky is good boy'
name='Venky is good boy'
name.title()
'Venky Is Good Boy'
name='Venky is good boy'
name.swapcase()
'vENKY IS GOOD BOY'
name='Venky is good boy'
name.casefold()
'venky is good boy'
#2. Alignment & Formatting Methods
name.center(30,'^')
'^^^^^^Venky is good boy^^^^^^^'
mame.center(20,'')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mame.center(20,'')
NameError: name 'mame' is not defined. Did you mean: 'name'?
mame.center(20,' ')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    mame.center(20,' ')
NameError: name 'mame' is not defined. Did you mean: 'name'?
name.center(20,'')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name.center(20,'')
TypeError: The fill character must be exactly one character long
'?
name.center(20,' ')
SyntaxError: unterminated string literal (detected at line 1)
name.center(30,' ')
'      Venky is good boy       '
name.ljust(30,' ')
'Venky is good boy             '
'?
name.ljust(20,'.')
SyntaxError: unterminated string literal (detected at line 1)
name.ljust(20,'.')
'Venky is good boy...'
'?
name.rjust(20,'.')
SyntaxError: unterminated string literal (detected at line 1)
name.rjust(30,'.')
'.............Venky is good boy'
'name'.ljust(30,' ')+':'
'name                          :'
'age'.ljust(30,' ')+'.'
'age                           .'
'phone number'.ljust(30,' ')+'.'
'phone number                  .'
'phone number'.rjust(30,' ')+'.'
'                  phone number.'
'56'.zfill(5)
'00056'
''.zfill(10)
'0000000000'
name
'Venky is good boy'
name.find('venky')
-1
name
'Venky is good boy'
name.find('a')
-1
name.find('e')
1
name.rfind('e')
1
name.rfind('y')
16
name.index('v')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    name.index('v')
ValueError: substring not found
name.index('e')
1
name
'Venky is good boy'
name.count.('o')
SyntaxError: invalid syntax
name.count('o')
3
name
'Venky is good boy'
'PFS30'.startswith('PFS')
True
l=['pfs20','pfs30','jsf22','ds40','pfs22']
l=['pfs20','pfs30','jsf22','ds40','pfs22']



l=['Demo.png','resume.pdf','index.webp','add.py','nul.py']
for i in l:
    i.endswith('png')

    
True
False
False
False
False
'abc'.alpha()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    'abc'.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
'abc'.isalpha()
True
'abc123'.isalpha()
False
'123'.isdigit()
True
'1.23'.isdigit()
False
'3+5+6'.isalnum()
False
'arun@123'.isalnum()
False
'arun123'.isalnum()
True
'Venky'.islower()
False
'venky'.islower()
True
'VENKY'.isupper()
True
name
'Venky is good boy'
' '.isspace()
True
name.istitle()
False
name1=name.istitle()
name1
False
name1=name.title()
name1
'Venky Is Good Boy'
name1.istitle()
True
'1.234'.isdecimal()
False
'4-34'.isnumeric()
False
'e23'.isnumeric()
False
'123'.isnumeric()
True
'myvar'.isidentifier()
True
'2'.isidentifier()
False
,,,
SyntaxError: invalid syntax
'''
a->z
b->y
o-%
u-6
'''
'\na->z\nb->y\no-%\nu-6\n'
name
'Venky is good boy'
name.translate(str.marketrans("abou","y%6"))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    name.translate(str.marketrans("abou","y%6"))
AttributeError: type object 'str' has no attribute 'marketrans'. Did you mean: 'maketrans'?
name.translate(str.marketrans("ebou","zs%6"))
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    name.translate(str.marketrans("ebou","zs%6"))
AttributeError: type object 'str' has no attribute 'marketrans'. Did you mean: 'maketrans'?
name.translate(str.marketrans("ecou", "zs%6"))
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    name.translate(str.marketrans("ecou", "zs%6"))
AttributeError: type object 'str' has no attribute 'marketrans'. Did you mean: 'maketrans'?
na,me
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    na,me
NameError: name 'na' is not defined
name
'Venky is good boy'
name.split(' ')
['Venky', 'is', 'good', 'boy']
>>> name.split('e')
['V', 'nky is good boy']
>>> name.rsplit()
['Venky', 'is', 'good', 'boy']
>>> name.rsplit(' ',2)
['Venky is', 'good', 'boy']
>>> names='venky','sangee','rajani'
>>> na,es.split(',')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    na,es.split(',')
NameError: name 'na' is not defined
>>> names.split(',')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    names.split(',')
AttributeError: 'tuple' object has no attribute 'split'
>>> names='venky','sangee','rajani'
>>> names.split(',')
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    names.split(',')
AttributeError: 'tuple' object has no attribute 'split'
>>> names='venky','rajani','sangee'
>>> names.split(',')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    names.split(',')
AttributeError: 'tuple' object has no attribute 'split'
>>> names.split(' , ')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    names.split(' , ')
AttributeError: 'tuple' object has no attribute 'split'
>>> names.split(' ')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    names.split(' ')
AttributeError: 'tuple' object has no attribute 'split'
