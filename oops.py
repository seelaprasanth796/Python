#oops
#syntax
'''class classname():
    #attributes
    name="lucky"
    age=25
    place="eg"
    def fname(method_name):
        print("statements.....")
a=classname()#a is object
print(dir(a))
a.fname()'''

#class declaration:
'''class Details():
    name="lucky"
    age=25
    place="EG"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation:
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("lucky",25,"EG")
a.display()
b=Details()
b.data("prasanth",27,"AP")
b.display()
c=Details()
c.data("lucky",28,"HYD")
c.display()'''

#object initialization:
'''class Data():
    #creating a constructor name (__init__):
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Data("lucky",25,"EG")
print(dir(a))
a.display()'''

#Task-1:
'''class Data():
    def __init__(self):
        self.name=input()
        self.age=int(input())
        self.place=input()
    def display(self):
        print(self.name,self.age,self.place)
a=Data()
print(dir(a))
a.display()'''

#method 2:
'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Data(name=input(),age=int(input()),place=input())
print(dir(a))
a.display()'''

'''n=list(map(int,input().split(',')))
target=int(input())
count=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==target:
            count.append([n[i],n[j]])
print(count)'''


#diff b/w _ and __ :when user want to create a variable in python by using (__) double reading underscore our python interpretor treats it as a special variable
#-to avoid name conplicts with methods in innner classes.

'''class employee():
    def __init__(self):
        self.name="Lucky"
        self._mailid="Lucky@gamil.com"
        self.__salary=10000
class employee1():
    def __init__(self):
        self.name="Prasanth"
        self._mailid="Prasanth@gamil.com"
        self.__salary=20000
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee__salary)
a=employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee1__salary)'''

#POLYMORPHISM:
#Operation overload
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(8))
print(a.__pow__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))

a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))

a="code";b="gana"
print(a.__add__(b))

a="python";b="course"
print(a.__add__(" "+(b)).title())'''


#operation overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
#x=A(6)#if we call inside the class it will print inside the function.
#y=B(4)
x=6#if we give value to object it will print outside the value.
y=4
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the prodcut is",a*b)
        else:
            print("program ends...")
a=new()
#a.sum()
#a.sum(3,4,5)
a.sum(3,4)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal make sounds")
class Dog():
    def speak(self):
        print("dog will bark")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


'''class car():
    def vehiclel(self):
        print("BMW")
class bike():
    def vehicle(self):
        print("Royal Enfeild")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#2.Inheritanse:
#single inheritance:single parent multiple child classes.
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("avaliable cash is",RBI.cash)
class SBI(RBI):#child class-1
    pass
class HDFC(RBI):#child class-2
    cash=50000
    def new_cash(cls):
        print("new cash",cls.cash+cls.cash)
        print("new cash",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''


#Multiple_inheritance:two parent class-one child class. 
'''class Father():
    def height(cls):
        a="165cm"
        print("height is",a)
class Mother():
    def weight(cls):
        b="55kgs"
        print("weight is",b)
class child(Father,Mother):
    def birth_date(cls):
        DOB="11-04-2001"
        print("the birth_date is",DOB)
x=child()
x.height()
x.weight()
x.birth_date()'''
 

'''class Father():
    def height(cls):
        print("height is 180cm")
class Mother():
    def weight(cls):
        b="55kgs"
        print("weight is 60kgs")
class child():
    def birth_date(cls):
        print("1 year kid")
a=Father()
b=Mother()
x=child()
a.height()
b.weight()
x.birth_date()'''


#Multi_level-inheritance:Grand parent to Parent to Child.
'''class Grand_parent():
    def land(cls):
        print("land is 1 acre")
class Parent(Grand_parent):
    def house(cls):
        print("house is 100sqft")
class child(Parent):
    def bike(cls):
        print("bike is Royal enfeild")
c=child()
c.land()
c.house()
c.bike()'''


#hierarichical inheritance:hierarichal inhertance is one parent class is inherited by multiple child classes.
'''class employee():
    def company_name(cls):
        print("Company name is Google")
class Trainer(employee):
    def teaching(cls):
        print("python")
class Developer(employee):
    def developing(cls):
        print("code")
a=employee()
a.company_name()
b=Trainer()
b.teaching()
b.company_name()
c=Developer()
c.developing()
c.company_name()'''

#hybrid:hybrid inheritance means combining one or morethan one type of inheritance.for example combining both hierarichal+multipe inheritance=hybrid.
'''class person():
    def details(cls):
        print("person details")
class trainer(person):
    def training(cls):
        print("trainer teaching the course")
class student(person):
    def learning(cls):
        print("student learning course")
class program_manager(trainer,student):
    def manage(cls):
        print("manager assigns classes")
a=program_manager()
a.details()
a.training()
a.learning()
a.manage()'''

#super():
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("Lucky",25)
print(a.age)
print(a.name)'''

#Encapsulation:combining multiple units into single unit is known it as a Encapsulation.
#publicdata
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
obj1=B()
obj1.method1()
obj1.method2()'''

#_protecteddata:
'''class A():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
obj1=B()
obj1.method1()
obj1.method2()'''

#__privatedata:
'''class A():
    __privatedata="Lucky"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj1=B()
obj1.method1()
obj1.method2()'''


#Abstraction:Abstraction hide in unnecasscary information From user is called a Abstraction.abstraction we have two types abstract class and abstract method.
        
#Abstract class:one or more abstract methods called abstract class
#Abstract method:the method is declared without implementation is called abstrct method.


'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''


'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''


'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("python course")
obj1=A()
obj1.method1()'''


'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        pass
    def method2(self):
        print("python full stack")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data structure")
    def method3(self):
        print("java full stack")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''


        




#Library management system:
'''1.add books-->option 1:python,java,dsa
2.display books-->option 2:show books
3.add a library member-->option 3:name,id
4.search book-->option 4:python
5.issue a book-->option 5:book issued
6.return a book-->option 6:return succesfully
7show member details-->show details
8.Exit-->stop'''


print("........Library Management System........")

class Library:
    def __init__(self, Books=None):
        if Books is None:
            self.Books = []
        else:
            self.Books = Books
        self.members = []
        self.issued_books = []

    def show_options(self):
        options = """1. Add books
                     2. Display books
                     3. Add a library member
                     4. Search a book
                     5. Issue a book
                     6. Return a book
                     7. Show member details
                     8. Exit"""
        print(options)

    def add_books(self):
        book_names = input("Enter book names to add: ")
        books = book_names.split(",")
        for book in books:
            book = book.strip()
            if book != "":
                self.Books.append(book)
        print("Books added successfully")

 
    def display_books(self):
        if len(self.Books) == 0:
            print("No books available")
        else:
            print("Books available in Library:")
            for book in self.Books:
                print(book)

    def add_member(self):
        name = input("Enter the name: ")
        member_id = input("Enter the ID: ")
        member = {"name": name,"id": member_id}
        self.members.append(member)
        print("Member added successfully")

    def search_book(self):
        book_name = input("Enter the book name: ")
        if book_name in self.Books:
            print("Book is available")
        else:
            print("Book is not available")

    def issue_book(self):
        book_name = input("Enter the book name to issue: ")
        if book_name in self.Books:
            if book_name in self.issued_books:
                print("Book is already issued")
            else:
                self.issued_books.append(book_name)
                print("Book issued successfully")
        else:
            print("Book is not available in library")

    def return_book(self):
        book_name = input("Enter book name to return: ")
        if book_name in self.issued_books:
            self.issued_books.remove(book_name)
            print("Book returned successfully")
        else:
            print("This book is not issued")

    def show_member_details(self):
        if len(self.members) == 0:
            print("No member registered")
        else:
            print("\nMember Details")
            for member in self.members:
                print("Name:", member["name"])
                print("ID:", member["id"])


library = Library()

while True:
    library.show_options()
    choice = input("Enter your choice:")

    if choice == "1":
        library.add_books()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.add_member()

    elif choice == "4":
        library.search_book()

    elif choice == "5":
        library.issue_book()

    elif choice == "6":
        library.return_book()

    elif choice == "7":
        library.show_member_details()

    elif choice == "8":
        print("Thank you... Exit")
        break

    else:
        print("Invalid choice...Select choice from 1 to 8")



































       









