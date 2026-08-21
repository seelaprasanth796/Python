#Type of loops in python.
#for,while,range,break,continue,pass.

#for loop> it is sequence iteration
'''a=[100,200,300,400]
for i in a:
    print(i)'''


'''a=[10,20,30,40]
for i in a:
    print(a)'''

'''a=[100,200,300,400]
for i in a:
    print(i,end=" , ")'''

'''a=[10,20,30,40]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''b=(1,2,3,4)
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''


'''c={1,2,3,4}
for i in c:
    print(i)
    print(type(c))
    print(type(i))'''

'''d={"name":"pooja","city":"vjw","state":"ap"}
for i in d:
    print(i)
    print(type(d))
    print(type(i))'''


#While loop > continous iteration
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=20
while a>2:
    a=a-1
    print(a)'''

'''a=20
while a>2:
    a=a-1
    print(a)'''

'''a=20
while a>2:
    a=a-1
print(a)'''

'''a=20
while a>5:
    print(a)
    a+=a'''

'''a=1
while a<30:
    print(a)
    a+=1'''

'''a=30
while a>5:
    print(a)
    a-=1'''

#voting
'''while True:
    age=int(input("Enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''

#Range()loop -----> the range function dones in sequence of numbers, starting from zero by default and increments by one by one and stops before a specified number.
#Range have three steps -----> start-stop-step

'''for i in range(11):
    print(i)'''

'''for i in range(5,20):
    print(i)'''

'''for i in range(0,20,2):
    print(i)'''

'''for i in range(5,50,5):
    print(i)'''

'''for i in range(3,30,3):
    print(i)'''

#task
'''while True:
a=int(input("enter the marks"))
if a in range(91,101):
          print("grade a")
elif a in range(81,91):
    print("grade b")
elif a in range(71,81):
    print("grade c")
elif a in range(61,71):
    print("grade d")
else:
    print("fail")'''

#break----> is used to terminate the entire loop.

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=20
while a>3:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(25):
    if i==10:
        break
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue----> is used to skips the curent iteration and rest of the code will continue.

'''a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue''' #in continue we will only write print after the continue only.


'''a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''

'''for i in range(15):
    if i==11:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''


#pass----> A pass is a null statement it does nothing but syntaxically we need.
          
'''a=9
while a>2:
    print(a)
    a=a-1
    if a==7:
        pass'''

'''for i in range(25):
    if i==20:
        pass
    print(i)'''


#Atm Application
'''while True:
        account=100000
        pwd=1234
        card=input("enter the card")
        if card=="c":
                print("welcome lucky")
                password=int(input("enter the password"))
                if password==pwd:
                             option=int(input("choose the option1.balance enq2.withdraw"))
                             if option==1:
                                print("acc bal is",account)
                             elif option==2:
                                     money=int(input("enter the amount"))
                                     print(money)
                                     balance=account-money
                                     print("rem bal is",balance)
                             else:
                                     print("invalid option")
                                     break
                else:
                        print("incorrect password")
        else:
                print("invalid card")'''
                                             
                                     













