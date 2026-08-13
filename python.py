#def a(): 
    ## print("hello world")
#def print_a():
    ##print(a())
#print_a()
"""x = int(input("ENTER A NUMBER:"))
res = 0
for i in range (1,x+1):
    res +=i*x
print(res)
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("Inpput a number"))))
import math
fact=math.factorial(4)
print(fact)"""
#simple interst 
"""p=int(input("Enter principle amount:"))
t=int(input("Enter the years:"))"""
'''x=int(98.6)

print(x)'''
"""print(35*2.75)
hrs = input("Enter Hours:")
h = float(hrs)
rate=float(10.50)
if h<=40:
    print(h*rate)
elif h>40:
    print(h*(1.5*rate)"""
"""for i in range(5):
    for j in range (i+1):
        print("*",end="")
    print()
class Dog:
    #methods
    def __init__(self,x):
        self.x=x
        print(x)
    def add(self,x1):
        self.x1=x1
        return x1+1"""
import asyncio
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def add_age(self,age):
        self.age=age+1
        

"""add=Dog(4)
add2=Dog(6)"""
"""cat=Cat("meow",3)
cat.add_age(3)

cat.get_name()
cat.get_age()
cat.add_age(5)
cat.get_age()
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__()"""
class Calculator:
    def __init__(self,x:int,y:int,op:str)->None:
        self.x=x
        self.y=y
        self.op=op
    def run(self)-> int:
        self.op=self.op.upper()
        if self.op[0]=="A":
            return self.x+self.y
        if self.op[0]=="M":
            return self.x*self.y
        
    def __str__(self):
        return str(self.run())
c= Calculator(4,5,"add")
c1=Calculator(9,3,"multi")

print(c1)


