#Functions:  1. A function is a block of organized and reuseable code,that is used to perform a single or multiple task.
            #2. Python gives in built functions like print,you can make your own function also,and these are user define functions.
            #3.Function blocks begin with the def , followed by the function name and paranthesis.

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#function:

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate (10,20)
calculate (100,200)
calculate (1000,2000)'''


# **,//,%:
'''def calculate(a,b):
    print("the pow is",a**b)
    print("the mod is",a%b)
    print("the intdiv is",a//b)
calculate (10,20)
calculate (10,20)
calculate (5,7)'''

'''def add(a,b):
    print(a+b)
add(5,6)'''

'''while True:
    def add():
        a=int(input("enter a value"))
        b=int(input("enter a value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    print(a+b)
    add()
add()'''

#Difference b/w Print and Return:
#PRINT >>>Print just shows the human user output in a console.
#RETURN>>>Return is a keyword and return is used to terminate the function and gives back a value from the function.

'''def mul(a,b):
    print(a*b)
mul(4,6)'''

'''def mul(a,b):
    return a*b
print(mul(4,5))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(5,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return (c) #in return it only print first value next two values terminate in return we can write in multiple lines.
    return (d)
    return (e)
print(cal(5,6))'''
    

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return (c,d,e) #in return we can write in all values in one return it will print all value.
print(cal(5,6))'''

#two methods add,sub,mul using single def and multiple def function: 
#1
'''while True:
    def add():
        a=int(input("enter the value"))
        b=int(input("enter the value"))
        option=int(input(....Values......
                        1.add
                        2.sub
                        3.mul))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    add()'''
        

#2
'''while True:
    def add():
        a=int(input("enter the value"))
        b=int(input("enter the value"))
        print(a+b)
    def sub():
        a=int(input("enter the value"))
        b=int(input("enter the value"))
        print(a-b)
    def mul():
        a=int(input("enter the value"))
        b=int(input("enter the value"))
        print(a*b)
    option=int(input(....Values......
                        1.add
                        2.sub
                        3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
    else:
        print("invalid")'''
        
#Split Bil:
#three methods separate 1.normal 2.fstring 3.format
#10 mem 20000bill separate each and every one split

#normal
'''a=int(input("total no of people"))
b=int(input("enter the total amount"))
c=b/a
print("per head",c)'''

#Fstring:
'''a=int(input("total no of people"))
b=int(input("enter the total amount"))
c=b/a
print(f"per head={c}")'''

#Format:
'''a=int(input("total no of people"))
b=int(input("enter the total amount"))
c=b/a
print("per head={}".format(c))'''

#functions:
'''def bill():
    a=int(input("total no of people"))
    b=int(input("enter the total amount"))
    c=b/a
    print("per head",c)
bill()'''



#Keyword and Positional arguments:

'''def Details(id,name,mailid):
    id=10
    name="lucky"
    mailid="l@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="lucky",mailid="l@gmail.com")
Details(40,"lucky","l@gmail.com")
Details("teja","l@gmail.com",50)
Details(name="lucky",mailid="l@gmail.com",id=20)'''


#default arguments:

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''


'''def Grocery(item="ghee", price):
#non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(1500)'''


#cake,price,quantity:

'''def Bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery("Caramel",500,"1kg")'''


'''def Bakery(cake="caramel",price=500,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery()'''


'''def Bakery(cake,price,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery("caramel",500)'''


'''def Bakery(cake="caramel",price=500,quantity): #error
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery("1kg")'''


# * arguments(* is used to unpack elements and as well as use in multiple functions):

'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''a=(10,20,30,40,50)
print(a)
print(*a)'''

'''a={10,20,30,40,50}
print(a)
print(*a)'''

'''a={"year":2021,"month":"august"}
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9 #error more than three variables we take.
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9 #we can use * arg to print value.
print(a)
print(*b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''


#Variable length arguments: Variable length arguments are automatically store in tuple we use in (*)arguments.

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,5,6,7,8]
check(*b)
c={6,7,8,9}
check(*c)
d={"city":"vjw","name":"lucky"}
check(*d)'''

'''def check1(*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.2,3.4)
check1(3,4,5,3.6,4.2,"lucky")'''


#Kwargs (**):keyword variable length arguments.
'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)'''


'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values:
        print(i)
    for i in a:
        print(a,a[i])
    for i in a.items:
        print(i)
check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)'''

#both * and ** usage:

'''def final(*a,**b):
    d=3 #creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("valuse is",j)
final()
data=(2,3,4,5,6.2)
final(*data)
details={"idnois":[1,2,3],"status":["p","a","p"]}
final(**details)
final(*data,**details)#this line prints both outputs.'''

#max(), min() ,sum():

'''print(max(5,7,8,9,10,40))
print(min(10,40,5,8,20))
a=[10,20,30]
b=sum(a)
print(b)'''

#Marks Analysis Report

'''n=int(input("number of students"))
a=[]
for i in range(1,n+1):
    b=int(input("enter the students marks"))
    a.append(b)
for i in a:
    print(i)
print(".......students report.....")
print("total students",n)
print("highest marks",max(a))
print("lowest marks",min(a))
print("total marks",sum(a))
print("average",sum(a)/n)'''


#GLOBAL and LOCAL Variables:Is also called as a Scope of variables.
#Global Variable: A variable is define above the function and is accesible to the entire global space is called Global Variable.
#Local Variable: A variable is defined inside the function is called Local Variable.

#First case of global variable
'''a=2
def check1():
    print("the inside value is",a)
check1()
print("the outside value is",a)'''


#second case of global variable
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("the outside value is",a)'''

#third case of global and local variable
'''a=5
def check3():
    a=6
    print("inside value is",a)
    a=10
    print("inside value is",a+5)
    b=12 #local variable
    b=b+a
    print("value of b is",b)
check3()
print("the outside value is",a)
print("the outside value is",b)'''#error bacause local variable is not def outside
          

'''a=5
b=8
def check3():
    a=6
    print("inside value is",a)
    a=10
    print("inside value is",a+5)
    b=12
    b=b+a
    print("value of b is",b)
check3()
print("the outside value is",a)
print("the outside value is",b)'''
                 
    
#usage of global keyword : When user want to create a variable inside function directly and carry farword the updated value and then we can use global keyword.

'''a=4
def final():
    global a,b #use global keyword to print the value of outside value
    print("inside value is",a)
    a=15 #global keyword is updated the value taken as a outside of a)
    print("updated value is",a)
    b=20
    b=b+a
    print("value is",b)
final()
print("outside the value is",a)
print("outside the value is",b)'''


#Generators : No tuple conprehension in above cases if we remove those braces and key paranthesis then outcome is Generator.
 #a=[expr for var in collection/range]
'''a=[i for i in range(16)] #list comprehension
print(a)'''

'''a=(i for i in range(16)) #Generators we can use in () circle.
print(*a)'''#generators are like packed we unpackes it to using (*).

'''a=(i for i in range(16)) 
#print(list(a)) #if we want to print in list we can use list.
#print(tuple(a)) #in generators we can print one datatype at a time.
print(set(a))'''

# Generators :A generator is also a function which cn be used as a (loop) by producing group of values we can use yield keyword
#Yield vs RETURN:Return will turminate the function where as yeild can pass the function and go on with every successive iteration. 
'''a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b: #while used in contious iteration
        yield a #yield gives two and it calls again the value print two times
        a=a+1
        yield a
print(*check(a,b))'''

    
'''a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a #if you give yield one time it will print all values one time.
print(*check(a,b))'''

'''a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        return a #in return it print only first value and terminates all values
print(check(a,b))'''#in return * arg is not used

#difference of return and yield.
'''def mygen():
    return "vjw"
    return "vzg"
    return "hyd"
    return "vjw","vzg","hyd"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())
# next()->>this keyword used to print value one by one.
a=mygen() #take input as one variable we can print three values using one variable name (a).
print(next(a)) #next() keyword only uses in yield not in return.
print(next(a))
print(next(a))'''

'''a=1
b=2
print(a,b)'''

'''a=input("enter the name")
print(a)'''

'''a=[1,2,3,4,5]
print(max(a))'''

'''a=[1,2,3,4,5]
print(min(a))'''

'''a=1
b=5
print(sum(a,b))'''

'''a=[1,2,3,4,5,6]
print(len(a))'''



'''a=[1,2,3,4,5,6]
print(len(a))
print(type(a))'''

'''a=10
for a in range(1,a+1):
    print(a)'''

'''a=5
print(pow(a))'''


#FROM KEYS(): fromkeys only used in dict().

'''a="codegnan"
print(a)
print(list(a))

print(tuple(a))

print(set(a))

# print(dict(a)) #error because in dict we can give both keys and values

#in dict we can print string using the (fromkeys):
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"lucky")
print(c)

c["o"]="python" #we can add word in keys in specific position
print(c)'''

#eval():
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b)'''

'''while True:
    a=eval(input("a value")) #eval() using to  print int,float,str,bool.
    b=eval(input("b value"))
    print(a+b)'''

#zip():we can combine multiple collections into one collection.

'''a=[10,20,30,40,50]
names=["sowmya","priya","kavya","preethi","harika"]
print(a+names)


a=[10,20,30,40,50]
names=["sowmya","priya","kavya","preethi","harika"]
print(a+names)

b=zip(a,names)#if we can use zip() to combine to collections we can use *arg or list,set,tuple,dict
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

d=(zip(a,names))
print(*d)'''

#enumerate()-> we can give counter to the collection:
'''names=["lucky","hemanth","sai","vasu","roop"]
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)'''


#Train Ticket
'''while True:
    ticket=1000
    gender=input("choose the gender male or female:")
    def male():
        age=int(input("enter the age"))
        if age>60:
                price=ticket*(30/100)
                print("ticket",price)
        else:
            print("ticket",ticket)
    def female():
        age=int(input("enter the age"))
        if age>60:
            price=ticket*(50/100)
            print("ticket",price)
        elif age<60:
            price=ticket*(30/100)
            print("ticket",price)
        else:
            print("ticket",ticket)
    if gender=="male":
        male()
    else:
        female()'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        
#Annonymous functions:Annonymous functions are name less function we use a keyword called as "lambda" to create annonymous functions.

#write a functoin to calculate 2*x+5 where x=5

'''def calculate():
    x=5
    c=2*x+5
    print(c)
calculate()'''

'''def f(x):
    print(2*x+5)
f(5)'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''


#tasks:
'''a="codegnan"
b=lambda a:a.upper()
print (b(a))'''

'''a="python course"
b=lambda a:a.title()
print(b(a))'''

#multyply:
'''a=2
b=4
c=lambda x:a*b
print(c(a))'''

'''a=int(input("enter a value"))
b=int(input("enter b value"))
c=lambda x:a*b
print(c(a))'''

#fname and lname using input and generator list comprehension method:
'''fname=input("enter the name")
lname=input("enter the name")
name=lambda fname,lname:fname+" "+lname
print(name(fname,lname))'''

'''a,b=[x for x in input("enter the name").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter():
#a=[10,20,30,43,54,60]
'''if a%2==0:#we can use for loop
    print(a)'''
'''for i in a:
    if a%2==0:
        print(i)'''
'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[ [],(),set(),{},"",None,3,5.6,"python",5+6j,True,False]
b=list(filter(None,a))
print(b)'''

#map ():Each object from a collection and form a new

'''a=[2,5,7,9,10,20,30,80]
b=[1,9,20,50,60,4,25,80]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

#string
'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the data").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the names").split(",")
print(a+b)'''

'''a,b=map(str,input("enter the data").split(",")
print(a+b)'''

#integer
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a,b=[int(x) for x in input("enter the data").split(",")]
print(a+b)'''

'''a=list(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a=tuple(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a=set(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a=input("enter the key and value")
b=dict(i.split(":") for i in a.split(","))
print(b)
print(type(b))'''

'''a=list(map(eval,input("values").split(",")))
print(a)
print(type(a))'''
           






























    

        



































      














































































    
