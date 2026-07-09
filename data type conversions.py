Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #data type
>>> #int
>>> int (4)
4
>>> int(8.9)
8
>>> int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
>>> int(5+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(2)
2.0
>>> float(5.0)
5.0
>>> float("hello")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
>>> float(5+6j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
float(False)
0.0

0
0

#str(string)
str(5)
'5'
str(5.8)
'5.8'
str(6+5j)
'(6+5j)'
str("python")
'python'
str(True)
'True'
str(False)
'False'

#complex
complex("prasanth")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("prasanth")
ValueError: complex() arg is a malformed string
complex(5)
(5+0j)
complex(5+6j)
(5+6j)
complex(5.0)
(5+0j)
complex(True)
(1+0j)
complex(False)
0j

#bool(boolean)
bool(5)
True
bool(5.8)
True
bool("prasanth")
True
bool(5+6j)
True
bool(True)
True
bool(False)
False
