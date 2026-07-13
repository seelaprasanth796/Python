Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#list
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>

#append
a=["python,css,java"]
a.append("html")
a
['python,css,java', 'html']
a.append["html,css"]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append["html,css"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(["html,css"])
a
['python,css,java', 'html', ['html,css']]

#extend
a=["html,css,java,"]
a.extend(["python,js"])
a
['html,css,java,', 'python,js']

#insert
b=["vja,rjy,hyd"]
b.insert(1,"chennai")
b
['vja,rjy,hyd', 'chennai']

#index
a=["apple","banana","grape"]
a.index("grapes")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.index("grapes")
ValueError: list.index(x): x not in list
a.index("grape")
2

 
#copy
a=["apple","banana","grape"]
a.copy()
['apple', 'banana', 'grape']
b=a.cpoy()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b=a.cpoy()
AttributeError: 'list' object has no attribute 'cpoy'
b=a.copy()

#lenghth
a=["apple","banana","grape"]
len(a)
3

len[a]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    len[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
d="apple"
len(d)
5

#sort
a=["mango","kiwi","dragon","berry"]
a.sort()
a
['berry', 'dragon', 'kiwi', 'mango']
a=[56,24,85,98,22,12,1]
a.sort()
a
[1, 12, 22, 24, 56, 85, 98]


#reverse
a=["ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds']
b=[2,3,4,5,6,7,8]
b.reverse()
b
[8, 7, 6, 5, 4, 3, 2]

#pop
a=["black","white","red","blue"]
a.pop(3)
'blue'
a
['black', 'white', 'red']
a.pop(0)
'black'
a

a.romove()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.romove()
AttributeError: 'list' object has no attribute 'romove'. Did you mean: 'remove'?
a.remove()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)

#clear
a=["ap","ts","ka"]
a.clear()
a
[]
b=[]
b.append()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b.append()
TypeError: list.append() takes exactly one argument (0 given)
b=[]
b.append("lucky")
b
['lucky']

>>> #TUPLES
>>> a=(4,6.7,"python",5+6j,True,False)
>>> print(a)
(4, 6.7, 'python', (5+6j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(8+9j)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.index(8+9j)
ValueError: tuple.index(x): x not in tuple
>>> a.index(8+9j)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.index(8+9j)
ValueError: tuple.index(x): x not in tuple
>>> a.index(5+6j)
3
>>> len(a)
6
>>> a.count(True)
1
>>> 
>>> #sets > it wil {} it is semi mutable
>>> a={4,6.7,"python",5+6j,True,False}
>>> print(a)
{False, True, 4, 6.7, (5+6j), 'python'}
>>> type(a)
<class 'set'>
>>> b={7,9,4,6,7,10,20,3}
>>> print(b)
{3, 4, 20, 6, 7, 9, 10}
>>> 
>>> #add
>>> a={1,2,3,4,5,6,7,8}
>>> b={5,6,7,8}
>>> a.add(15)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 15}
>>> 
#issubset
a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9}
b.sibset(a)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    b.sibset(a)
AttributeError: 'set' object has no attribute 'sibset'
b.subset(a)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    b.subset(a)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9}
SyntaxError: multiple statements found while compiling a single statement
a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8}
SyntaxError: multiple statements found while compiling a single statement

a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9}
SyntaxError: multiple statements found while compiling a single statement
#superset
a=
SyntaxError: invalid syntax
a={1,2,3,4,5,6}
b={3,4,5,6}
b.issuperset(a)
False
a.issuperser(b)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a.issuperser(b)
AttributeError: 'set' object has no attribute 'issuperser'. Did you mean: 'issuperset'?
a.issuperset(b)
True

#union
a={3,4,5,6,7}
b={1,2,3,4,5,6,7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7}

#intersection
a={3,4,5,6,7}
b={1,2,3,7,5,6}
SyntaxError: multiple statements found while compiling a single statement
a={3,4,5,6,7}
b={1,2,3,7,8,9}
a.intersection(b)
{3, 7}
b.intersection(a)
{3, 7}

#differnce
a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
a.differnce(b)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    a.differnce(b)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
SyntaxError: multiple statements found while compiling a single statement
a={7,8,9,10}
b={7,8,9,10,11,12}
a.difference(b)
set()

#update
a={2,3,4,5,6}
b={1,4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{1, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#simmetric
a={1,2,3,4,5,6,7,8}
b={2,4,6,7,9,20}
a.symmetric_difference(b)
{1, 3, 5, 8, 9, 20}

#difference_update
a={4,5,6,7,8,9}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7, 8, 9}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 10}

#intersection_update
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}

#symmetric_difference_update
a={11,12,13,14,15,16}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{17, 18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}

#pop
a={3,4,5,6,7,8}
a.pop()
3
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.romove(4)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    a.romove(4)
AttributeError: 'set' object has no attribute 'romove'. Did you mean: 'remove'?
a.remove(6)
a
{4, 5, 7, 8}

#copy
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}

a.discord(50)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a.discord(50)
AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
a={10,20,30,40,50}
a.discard(50)
a
{20, 40, 10, 30}
a.clear()
a
set()
b=set()
b.add(100)
b
{100}

#disjoint
a={1,2,3,4,5}
b={6,7,8,9,10}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
True
b.isdisjoint(a)
True
a={1,2,3,4,5}
b={1,2,3,4,5}
a.isjoint(b)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    a.isjoint(b)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
