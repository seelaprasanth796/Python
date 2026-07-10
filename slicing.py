Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> 
>>> #task 1 positive slicing
>>> a="work untill you succeed"
>>> a[0:4]
'work'
>>> a[6:11]
'ntill'
>>> a[6:12]
'ntill '
>>> a[6:13]
'ntill y'
>>> a[5:12]
'untill '
>>> a[16:23]
'succeed'
>>> a[12:15]
'you'
>>> 
>>> a="time is very precious"
>>> a[13:21]
'precious'
>>> a[8:12]
'very'
>>> a[0:4]
'time'
>>> 
>>> #Negative indexing
>>> a="simple is better than complex"
>>> a[-20:-14]
' bette'
>>> a[-20:-13]
' better'
>>> a[-30:-23]
'simple'
>>> a[-8:-0]
''
>>> a[-8:-1]
' comple'
>>> a[-8:1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[-8:1]
''
>>> a[-8:0]
''
>>> a[-7:-0]
''
>>> a[-7:-1]
'comple'
>>> 
>>> 
>>> 
>>> 
>>> b="codegnan it solutions"
>>> b[-22:-13]
'codegnan'
>>> b[-9:-1]
'solution'
b[-9:]
'solutions'
