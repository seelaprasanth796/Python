Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#string methods
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e="i am in vjw"
len(e)
11

#count
#count
#methods are not taken directly count is a method so we can take as a.count
a="twinkle twinkle littile star"
count(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3

#find a string



a="python"
a.find("h")
3
b="hello world"
b.find("l")
2

#escape sequences
#\n > new line or next tab
#\t > tab space
a="name\nemail id\ncollege\tcourse\n mobile number
SyntaxError: unterminated string literal (detected at line 1)
a="name\nemail id\tcollege\ncourse"
print(a)
name
email id	college
course

a="name:prasanth\ncollege:VSM\tcourse:mca\nmobilenumber:0878656755"
print(a)
name:prasanth
college:VSM	course:mca
mobilenumber:0878656755

#replace
a="wait untill you succed"
a.replace("wait","work")
'work untill you succed'

b="python java")
SyntaxError: unmatched ')'
b="python java"
b.replace("P","c")
'python java'
c.replace("p","c")
''
c="wait wait untill you succeed"
c.replace("wait","work")
'work work untill you succeed'
c="wait wait untill succeed"
c.replace("wait","work",1)
'work wait untill succeed'

#uppercase()
a="code"
a.upper()
'CODE'

#lowercase()
b="CODE"
b.lower()
'code'

#capitalize > it will only use the first letter will be capital
c="iam in python class"
c.capitalize()
'Iam in python class'

#title > it will use to every word in the fisrt letter will be capital
d="iam in the python class"
d.title()
'Iam In The Python Class'

#conditional
a="code'
SyntaxError: unterminated string literal (detected at line 1)
a="code"
a.isalpha()
True

b="python"
b.islower()
True
b.isupper()
False

c="code"
c.isdigit()
False

d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True

#alnum > it takes alphabets and numerics
a="prasanth1122"
a.alnum()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
a="prasanth1122"
a.isalnum()
True

b="prasanth@1122"
b.isalpha()
False

#startswith
a="codegnan"
a.isstartwith(c)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.isstartwith(c)
AttributeError: 'str' object has no attribute 'isstartwith'. Did you mean: 'startswith'?
a="codegnan"
a.startwith(c)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.startwith(c)
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a="codegnan"
a.startswith(c)
True
a.endswith(n)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.endswith(n)
NameError: name 'n' is not defined
a="codegnan"
a.endswith(n)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.endswith(n)
NameError: name 'n' is not defined
a="lucky"
a.endswith("y")
True

#strip > it will removes spaces
#it have two types: lstrip > it remove leftside space , rstrip> it will remove right side strip
a="   lucky   "
a.strip()
'lucky'
a.lstrip()
'lucky   '
a.rstrip()
'   lucky'

#split()
a='python java c"
SyntaxError: unterminated string literal (detected at line 1)
a="python c java"
a.split()
['python', 'c', 'java']

b="kider joy"
b.split()
['kider', 'joy']

#join()
b="html","java","js"
"".join(b)
'htmljavajs'
" ".join()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    " ".join()
TypeError: str.join() takes exactly one argument (0 given)
b="java","css","js"
" ".join(b)
'java css js'
"k".join(b)
'javakcsskjs'

#concatenation
a="code"
b="gnan"
print(a+b)
codegnan

a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course

fname="prasanth"
lname="l"
print(fname+lname)
prasanthl
print(fname.title()+" "+lname.title())
Prasanth L
print((fname+" "+lname).title())
Prasanth L

#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12

city="vjw"
print("the city is",city)
the city is vjw

#format
>>> #format
>>> a="motu"
>>> b="pathulu"
>>> print("hello {}{}".format(a,b))
hello motupathulu
>>> print("hello {} {}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    print("hello {} {}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> a="motu"
>>> b="pathulu"
>>> print("hello {} {}".format(a,b))
hello motu pathulu
>>> print("hello {}\n{}".formar(a,b))
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    print("hello {}\n{}".formar(a,b))
AttributeError: 'str' object has no attribute 'formar'. Did you mean: 'format'?
>>> a="motu"
... b="pathulu"
SyntaxError: multiple statements found while compiling a single statement
>>> a="motu"
... b="pathulu"
... print("hello {}\n{}".format(a,b))
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> #fstring()
>>> a="sita"
>>> b="rama"
>>> print(f"hello {a} {b}")
hello sita rama
>>> print(f"hello {a}{b}")
hello sitarama
>>> print(f"hello {a} hello {b}")
hello sita hello rama
>>> print(f"hello {a} \nhello{b}")
hello sita 
hellorama
