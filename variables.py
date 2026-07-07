Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#Variables
proint(6+8)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    proint(6+8)
NameError: name 'proint' is not defined. Did you mean: 'print'?
print(6*8)
48
a=4
b=6
print(a+b)
10

c=30
print(c)
30
z=30
print(Z)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
print(z)
30
x=50
print(x)
50
name="prasanth
SyntaxError: unterminated string literal (detected at line 1)


name="prasanth"
print(name)
prasanth
print("name)
      
SyntaxError: unterminated string literal (detected at line 1)
print("name")
      
name
city("vjw")
      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    city("vjw")
NameError: name 'city' is not defined
city=("vjw")
      
print(city)
      
vjw
2=30
      
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2=30
      
print(a2)
      
30
4a=30
      
SyntaxError: invalid decimal literal
a123456=100
      
print(a123456)
      
100
#special characters
      
@=50
      
SyntaxError: invalid syntax
$=30
      
SyntaxError: invalid syntax
_d=20
      
print(_d)
      
20
 f=90
      
SyntaxError: unexpected indent
#keyword it will aloows keywords
      
if=60
      
SyntaxError: invalid syntax
first name="prasnth"
      
SyntaxError: invalid syntax
first_name="prasanth"
      
print(first_name)
      
prasanth
firstname="prasanth"
      
print(firstname)
      
prasanth

#single line two variables separate with cama
      
a=4,b=9
      
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
      
print(a+b)
      
13
a,b=5,6
      
print(a,b)
      
5 6

#single line multiple variables
      
a=2,3,4,5,6,7,8
      
print(a)
      
(2, 3, 4, 5, 6, 7, 8)
a,b,c=2,3,4
      
>>> print(a,b,c)
...       
2 3 4
>>> a,b,c=5,6,7,8,9
...       
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a,b,c=5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 5)
>>> #unpacking
...       
>>> a,b,c=(6,7,8)
...       
>>> print(a,b,c)
...       
6 7 8
>>> #del keyword
...       
>>> a=6
...       
>>> print(a)
...       
6
>>> del a
...       
>>> print(a)
...       
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a2'?
>>> 
>>> #usecase
...       
>>> fname="prasanth"
...       
>>> lname="s"
...       
>>> print(fname+lname)
...       
prasanths
>>> print(fname+ lname)
...       
prasanths
>>> print(fname+" "+lname)
...       
prasanth s
>>> print(fname,lname)
...       
prasanth s
>>> #case sensitive
...       
>>> name="prasanth"
...       
>>> print(name)
...       
prasanth
>>> NAME="prasanth"
...       
>>> print(NAME)
...       
prasanth
>>> Name="prasanth"
...       
>>> print(Name)
...       
prasanth
