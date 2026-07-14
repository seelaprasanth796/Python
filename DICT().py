Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#dict{} > it is taken as key and value
a={"name":"lucky","year":2026,"month":a}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a={"name":"lucky","year":2026,"month":a}
NameError: name 'a' is not defined
a={"name":"lucky","year":2026,"month":7}
print(a)
{'name': 'lucky', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['lucky', 2026, 7])
a.items()
dict_items([('name', 'lucky'), ('year', 2026), ('month', 7)])

#update > we add one or more with using {,}
a={"year":2026,"month":"july","date":14}
a.update()
a
{'year': 2026, 'month': 'july', 'date': 14}
a.update({"day":"tuesday"})
a
{'year': 2026, 'month': 'july', 'date': 14, 'day': 'tuesday'}
a.update({"day":"tuesday"},{"time":2})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.update({"day":"tuesday"},{"time":2})
TypeError: update expected at most 1 argument, got 2
a.update({"day":"tuesday","time":2})
a
{'year': 2026, 'month': 'july', 'date': 14, 'day': 'tuesday', 'time': 2}

#setdefault > it will add given value as setdefault
a={"name":"lucky","city":"vjw"}
a
{'name': 'lucky', 'city': 'vjw'}
a.setdefault("mail","lucky@gmail.com")
'lucky@gmail.com'
a
{'name': 'lucky', 'city': 'vjw', 'mail': 'lucky@gmail.com'}


#pop> del particular value was given as a key
a={"country":"india","state":"ap"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("country")
'india'

#popitem()> it will remove value without given key it del both key and value
>>> a={"country":"india","state":"ap"}
>>> a.popitem()
('state', 'ap')
>>> a.popitem()
('country', 'india')
>>> a
{}
>>> 
>>> #dict() it doesnot have any duplicates it will given as key different name it will takes.we given as a key different and value same it will take
>>> 
>>> #COPY()
>>> a={"colour":"black","food":"biryani"}
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> b=a.copy()
>>> a
{'colour': 'black', 'food': 'biryani'}
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> b=a.copy()
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> len(a)
2
>>> 
>>> 
>>> #dupliucate
>>> a={"name":"lucky","city":"vjw","name":"lucky"}
>>> print(a)
{'name': 'lucky', 'city': 'vjw'}
>>> a={"name1":"lucky","city":"vjw","name2":"lucky"}
>>> print(a)
{'name1': 'lucky', 'city': 'vjw', 'name2': 'lucky'}
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.index()
AttributeError: 'dict' object has no attribute 'index'
>>> #count and index not in DICT it only in sets and lists.
>>> 
>>> #clear
>>> a.clear()
>>> a
{}
>>> #if we want to add item after clear we use update()
>>> b={}
>>> b.update({"name":"lucky"})
>>> b
{'name': 'lucky'}
>>> 
>>> #single key how we add multiple values in using DICT
>>> a={"idnod":[10,20,30],"names":["lucky","prasanth"],"marks":[10,20,30]}
>>> print(a)
{'idnod': [10, 20, 30], 'names': ['lucky', 'prasanth'], 'marks': [10, 20, 30]}
>>> a.keys()
dict_keys(['idnod', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['lucky', 'prasanth'], [10, 20, 30]])
>>> type(a)
<class 'dict'>
>>> a.items()
dict_items([('idnod', [10, 20, 30]), ('names', ['lucky', 'prasanth']), ('marks', [10, 20, 30])])
