Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import keyword
from keyword import kwlist
print(kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
a=10
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a
10
b
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b
NameError: name 'b' is not defined
a,b,c=10,20,30
a
10
b
20
c
30
a,b=b,a
a
20

b
10
a=b=10
a
10
b
10
a=10
b=20
print("addition")
addition
print("addition",a+b)
addition 30
print("division")
division
>>> print("division",a-b)
division -10
>>> 10
10
>>> #1.addition of two numbers
>>> #2.keywords
>>> import keyword
... 
... print(keyword.kwlist) # List of all keywords
... print(len(keyword.kwlist))
SyntaxError: multiple statements found while compiling a single statement
>>> import keyword
... 
... print(keyword.kwlist) 
... print(len(keyword.kwlist))
SyntaxError: multiple statements found while compiling a single statement
>>> import keyword
... 
... print(keyword.kwlist) 
... print(len(keyword.kwlist))
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> import keyword
>>> print (keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> '''
... print(keyword.kwlist)
... '''
'\nprint(keyword.kwlist)\n'
