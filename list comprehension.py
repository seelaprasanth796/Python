#list comprehension---> Every comprehension re-written as a for loop.But every for lopp cannot be re-written in list comprehension.
a=["python","java","dsa"]
#["PYTHON","JAVA","DSA"]
#print(a.upper()) #error

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

#Tasks
'''a=["codegnan","course","python"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,3,4,5,6,8,12,13]
b=[pow(i,2) for i in a]
b=[i*i for i in a]
b=[i**2 for i in a]
print(b)'''


#if-usage in list comprehension:
'''a=[i for i in range(0,21) if i%2==0]
print(a)'''#even

'''a=[i for i in range(0,21) if i%2!=0]
print(a)''' #odd

'''a=[i*i for i in range(0,21) if i%2==0]
print(a)'''#even num square

'''a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" in i]
print(b)'''#print only a letter fruits

'''a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" not in i]
print(b)''' #print a not in letter fruits

#no-elif usage in list comprehension.

#if-else usage in list comprehension.

'''a=[i**2 if i%2==0 else i*5 for i in range(16)]
print(a) '''   #use if and else in list even numbers are divisible by 5


'''a=[1,2,3,4,5] 
b=[5,4,3,2,1]
#[6,6,6,6,6,6]
#c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

#Report of Attendence Report
'''students=int(input("enter the total no of students"))
p=0
a=0                       
for i in range(1,students+1):
    attendence=input(f"student{i} (p/a)")
    if attendence=="p":
        p+=1
    elif attendence=="a":
        a+=1
print(".......attendence........")
print("total students attendence",students)
print("total students present",p)
print("total students absence",a)'''
    
        

