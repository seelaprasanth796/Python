#Difference b/w module , library , package:

#MODULE():A module in python is a single python file it consists python code.
#examples of modues math.py and random.py and my module.py
#A python contains classes,functions and variable.

#PACKAGE():A package one or more python modules and contains __init__.py file.(__ double underscore)
#Examples of packages include requests, numpy, pandas.

#LIBRARY():A library consits both modules and packages.
#Examples of library such as numpy,pandas,and matplotlit.

#NOTE : Every python files a module and import is a keyword and every python file is saves internally with variable name as __main__.



'''def greetings(name):
    print("welcome",name)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''


#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.cos(30))
print(math.sin(60))
print(math.ceil(2.9))
print(math.ceil(5.9))
print(math.ceil(8))
print(math.floor(2.7))'''

#from keyword:
'''from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''

#sys module:
'''import sys
print(sys.path)
print(sys.version)'''

#os module:
'''import os
print(os.path)
print(os.getcwd)
print(os.listdir)'''

'''print(os.mkdir("aug4"))
print(os.listdir)'''

'''print(os.chdir("c:\\User\\Admin\\Downloads"))
print(os.listdir())'''

#ASCII:american system coding
'''print(chr(67))

print(chr(65)) #chr only print number
print(chr(90))
print(chr(93))

print(ord("a"))#ord only print character
print(ord("A"))'''

'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,122):
    print(chr(i),end=" ")'''

#task enter name and assign number to that letter:
'''a=input("enter name")
b=[]
for i in a:
    b.append(ord(i))
print(a,b)'''

'''a=input("enter name")
for i in a:
    print(i,ord(i))'''

#random module: Random module is used to generate random numbers in python, randint function is used.And this function is used in random module.
#sample
'''import random
a=random.sample(range(10,50),5)
print(a)'''

#randint()
'''import random
a=random.randint(40,50)
print(a)'''

#choice()
'''import random
a=[10,40,50,70,90]
b=random.choice(a)
print(b)'''

#dice
'''import random
while True:
    roll_of_dice=int(input("enter the number"))
    dice=random.randint(1,6)
    print(dice)
    option=input("roll again (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid")'''

#calendar
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#date and time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"today time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")

print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''
    
    
    
'''import random
import time
for i in range(10):
    print(random.randint(1,10))
    time.sleep(2)'''


#regex(regular expressions):regular expressions powerful tools(module,embeded in python)which is mainly used to find a pattern
#-with in a given strings are statements are mainly used for text manipulation.

'''a="codegnan is in vjw"
print(a)'''

'''a="codegnan\nis\tin\nvjw"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvjw"
print(a)'''

#compile(),search(),findall(),split(),sub
#sequence character
'''\w>it matches alphnumeric
\W>it matches non alpha numeric
\d>it matches any digit
\D>it matches non digits
\s>it represents white spaces
\S>it represents non white spaces.'''

#compile()
'''import re
a="map maths cat code money mat cup cap monkey"
b=re.compile(r"m\w\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''b=re.search(r"m\w+",a)
print(b)'''

#findall()
'''c=re.findall(r"m\w+",a)
print(c)'''


'''d=re.findall(r"c\w+",a)
print(d)'''

#split()
'''e=re.split(r"m",a)
print(e)

f=re.split(r"\S",a)
print(f)

f=re.split(r"\s",a)
print(f)'''


#sub
'''g=re.sub(r"m","a",a)
print(g)'''

#digit
'''import re
a="lucky1122"
b=re.compile(r"1\d")
print(b)

c=b.search(a)
print(c)

d=re.findall(r"\d+",a)
print(d)'''

#error Handling
'''1.syntax error--->compile error.

2.Run_time error----> During execution time it will happens.

3.Logical error----> Error in logic(it cant be visible).

#syntax error
for i in range(10) #syntax error
print(i) 


#runtime_error
a=int(input("a value")
b=int(input("b value")
print(a//b) #error 10//0  --> zero division error   
      
#logical error
a=10
b=20
print(a-b)'''

#EXCEPTION HANDLING:
#try: instructions from which we are expecting the exceptions
#except: exceptions are raised in try block it will be handle by this block.
#else->no exceptions(optional)
#finally:always it will display.

#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("program ends......")'''

#file handling
#write()
'''a=open("lucky.txt","w")
b=a.write("python full stack")
a.close()'''

'''a=open("lucky.txt","w")
b=a.write("codegnan it solutions")
a.close()'''
      

#append()
'''a=open("lucky.txt","a")
b=a.write("\tLucky")
a.close()'''

'''a=open("lucky.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("lucky.txt","w")
b=input("data")
a.write(b)
a.close()'''

'''a=open("lucky.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read lines():
'''a=open("lucky.txt")
print(a.read())#it will display entire content
print(a.readline())#it only display first line
print(a.readlines())#it will display in list with \n
print(a.read(7))#it will display no.of characters'''

#writelines()--> it makes every object side by side
'''a=open("prasanth.txt","w")
b=["lucky","sai","krishna","roop","vasu"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("data.py")
print(a.read())'''











































































































































