Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#positive indexing
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[1]
' '
a[1]+a[4]+a[7]
'   '

#task 1
a="i am learing python"
a[14]+a[15]+a[16]+a[17]+a[18]+a[10]
'ythonn'
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
'python'
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]
'learing'
>>> 
>>> #task 2
>>> a="i love codegnan"
>>> a[7]+a[8]+a[9]+a[10]
'code'
>>> a[2]+a[3]+a[4]+a[5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[2]+a[3]+a[4]+a[5]
'love'
>>> a[11]+a[12]+a[13]+a[14]
'gnan'
>>> 
>>> #Negative indexing
>>> a="vijayawada is a royal city"
>>> a[-10]+a[-9]+a+[-8]+a[-7]+a[-6]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[-10]+a[-9]+a+[-8]+a[-7]+a[-6]
TypeError: can only concatenate str (not "list") to str
>>> a[-6]+a[-7]+a[-8]+a[-9]+a[-10]
'layor'
>>> a[-10]
'r'
>>> a[-10]/a[-9]/a[-8]+a[-7]+a[-6]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[-10]/a[-9]/a[-8]+a[-7]+a[-6]
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[6]
'royaw'
>>> a[-12]
'a'
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]+a[-20]+a[-19]+a[-18]+a[-17]
'vijayawada'
