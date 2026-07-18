#if_elif conditions by using comparision

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")'''

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

#if-elif-else
'''a=5
b=10
if a>b:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("equal")'''

'''a=5
b=10
if a>b:
    print("greater")
elif a>=b:
    print("equal")
else:
    print("not equal")'''

'''a=5
b=10
if a<b and b>a:
    print("greater")
elif a!=b or a==b:
    print("equal")
else:
    print("not equal")'''

'''a=int(input("a value"))
if type(a) is int:
    print("it is int")
else:
    print("not int")'''

#multiple if
'''a=9
b=11
if a<b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''

'''a=9
b=11
if a>b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")
if a!=b:
    print("not equal")'''

#nested if
'''a=2
b=4
if a<b:
    print("less")
    if b>a:
        print("greater")'''


'''a=2
b=4
if a==b:
    print("less")
    if b>a:
        print("greater")'''


'''a=2
b=4
if a<b:
    print("less")
    if b<a:
        print("greater")'''


'''a=2
b=4
if a>b:
    print("less")
    if b>a:
        print("greater")   
else:
    print("true")'''

'''a=2
b=4
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")'''

'''a=2
b=4
if a<b:
    print("less")
    if b<a:
        print("greater")
    elif a!=b:
        print("true")'''


#Tasks

'''age=int(input("enter age"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''

'''a=int(input("enter the value"))
if (a%2==0):
    print("even")
else:
    print("odd")'''

'''year=int(input("enter the year"))
if year%4==0:
         print("it is leap year")
else:
    print("it is not leap year")'''

#string
'''name=input("enter the name")
if name=="lucky":
    print("welcome lucky")
else:
    print("welcome guest")'''

'''name=["lucky","prasanth","eswar"]
a=input("enter the name")
if a in name:
    print("welcome")
else:
    print("guest")'''

'''letter=["a","e","i","o","u"]
a=input("enter the letter")
if a in word:
    print("vowels")
else:
    print("consonant")'''

#nested if
#social media-login

'''a=input("username")
b=int(input("password"))
if a=="lucky":
    print("login")
    if b==1234:
        print("login")
else:
    print("invalid")'''

'''a=input("username")
b=input("password")
if a=="lucky" and b==1234:
    print("login")
else:
    print("invalid")'''

'''a=input("username")
b=int(input("password"))
if a=="lucky":
    if b==1234:
        print("login")
    else:
        print("incorrect password")
else:
    print("invalid")'''

#multiple if
'''age=int(input("enter the age"))
marks=int(input("enter the marks"))
attendence=int(input("enter the number"))
if age>=18:
    print("eligible for vote")
if marks>=70:
    print("allow to write exams")
if attendence>=80:
    print("they are eligible")'''

#if-elif-else
'''cake=input("enter the name")
if cake=="red_velvet":
    print("1200")
elif cake=="choco_almond":
    print("1000")
elif cake=="honey_almond":
    print("800")
elif cake=="butter_scotch":
    print("600")
else:
    print("cake is not available")'''


'''pizza=int(input("enter the value"))
if pizza==1000:
    print("BBQ PIZZA")
elif pizza==800:
    print("Crispy chicken pizza")
elif pizza==400:
    print("Panner pizza")
elif pizza==200:
    print("frenchfries and coke")
else:
    print("pizza not available")'''

