Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'tarak is good boy'
name.upper()
'TARAK IS GOOD BOY'
name. lower()
'tarak is good boy'
name.capitalize()
'Tarak is good boy'
name.tittle()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
name.swapcase()
'TARAK IS GOOD BOY'
name.title()
'Tarak Is Good Boy'
name.casefold()
'tarak is good boy'
name.center(40,' ')
'           tarak is good boy            '
name.center
<built-in method center of str object at 0x00000212A726D200>
name.center(60,'-')
'---------------------tarak is good boy----------------------'
name.ljust(30,' ')+':'
'tarak is good boy             :'
'tarak is good boy             :'
'tarak is good boy             :'
name.find(good)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name.find(good)
NameError: name 'good' is not defined
name.find('good')
9
name.find('a')
1
name.rfind('good')
9
name.rfind('boy')
14
name.index('tarak')
0
name.index('rak')
2
name.index('rk')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    name.index('rk')
ValueError: substring not found
name
'tarak is good boy'
name.count('good')
1
name.count('o')
3
name.index('z')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name.index('z')
ValueError: substring not found
name.find('find')
-1
'pfs'.startswith('pfs')
True
'pfs40'.startswith('40')
False
l=['pfs40','ds30','pfs50']
for i in l:
    if i.endswith('0'):
        print(i)

...         
pfs40
ds30
pfs50
>>> name
'tarak is good boy'
>>> name.islower()
True
>>> name.isalpha()
False
>>> name.isnum()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    name.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> name.isnumeric()
False
>>> nmae.isalnum()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nmae.isalnum()
NameError: name 'nmae' is not defined
>>> '123'.isnumeric()
True
>>> 'pardhu'.isidentifier()
True
>>> 
>>> name
'tarak is good boy'
>>> name.replace('tarak','pardhu')
'pardhu is good boy'
>>> name.split(' ')
['tarak', 'is', 'good', 'boy']
>>> name.split()
['tarak', 'is', 'good', 'boy']
>>> name.split('.')
['tarak is good boy']
>>> name.split('/')
['tarak is good boy']
