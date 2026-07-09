Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#operators
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a**b)
16
print(a/b)
0.5
print(a//b)
0
print(a%b)
2

#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=b
a
3
a*=4
a
12
a**=3
a
1728
a//=5
a
345
a%=3
a
0
a/=1
a
0.0

a+=b
b
5
a-=b
b
5
a*=b
b
5
a**=b
b
5
a?=b
SyntaxError: invalid syntax
b
5
a/=b
b
5
a//=b
b
5
a%=b
b
5

#comparison
a=6
b=8
a<b
True
b>a
True
a<=b
True
a>=b
False
b>=a
True
a==b
False
b==a
False
a!=b
True

#logical
a=4
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a!=b or a==b
True
not True
False
not False
True

#identify
a=6
type(a) is int
True
type(a) is not int
False
b=5.7
type(b) is float
True
c=("lucky")
type(c) is str
True
d=5+6j
type(d) is complex
True
f=true
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    f=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> f="True"
>>> type(f) is bool
False
>>> f=True
>>> type(f) is bool
True
>>> 
>>> #membership
>>> a=2,3,4,5,6,7,8,9
>>> 9 in a
True
>>> 10 in a
False
>>> 10 is not a
True
>>> 1 is not in a
SyntaxError: invalid syntax
>>> 1 is not a
True
>>> 
>>> #bitwise
>>> a&b
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a&b
TypeError: unsupported operand type(s) for &: 'tuple' and 'float'
>>> a=4
>>> b=6
>>> a&b
4
>>> bin(4)
'0b100'
>>> bin(6)
'0b110'
>>> 
>>> a=7
>>> b=9
>>> a&b
1
>>> bin(7)
'0b111'
>>> bin(9)
'0b1001'
>>> 
>>> a=4
>>> b=5
>>> a|b
5
>>> 
>>> #not
>>> a=6
>>> -(a+1)
-7
>>> ~a
-7
>>> b=-5
>>> ~b
4
>>> 
>>> #xor
>>> a=6
>>> b=6
>>> a^b
0
>>> 
