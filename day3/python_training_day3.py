""" WHAT IS THE IMPORTANCE OF OBJECT ORIENTED PROGRAMMING IN DEVELOPMENT?   
"""

# data members - represent 
# action on those data
# self variable - by using self variable we pointing to the current object

# difference between function and method
# function is the block of code that is written outside the class 
# method is the block of code that is written inside the class

# class
# class Student:
#     roll_no = 101
#     num1 = 50
#     num2 = 100
    
#     def ad(self):
#         print(self.num1+self.num2)
#         self.name=input("Enter name: ")
#         print(self.name)
        
# obj = Student()
# obj.ad()
# print(obj.roll_no)

# constructor - is a special type of method that is used to initialize the memory othe object 
# class NewClass:
#     def __init__(self):
#         print("my name is constructor")
#     def show(self):
#         print("Welcome to class")
# obj = NewClass()
# print(obj)       #<__main__.NewClass object at 0x00000160A99E6A50>  -- hexa code
# obj.show()


# default constructor
# class Hod:
#     def __init__(self):
#         self.name = "Vihas"
#         self.age = 53
#         self.empid = 1001
#     def info(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         print("Emp ID: ",self.empid)
        
# obj = Hod()
# obj.info()

# parameterized constructor
# class Hod:
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age = age
#         self.empid = rollno
#     def info(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         print("Emp ID: ",self.empid)
        
# obj = Hod('Arjun',45,101)
# obj.info()

# Types of variable used in class 
# 
#  - Instance variable: this variable is 
# class Student:
#     def __init__(self):
#         self.name = "Vihas"
#         self.roll = 101
        
#     def getdata(self):
#         self.s_mb = 100 
        
# obj = Student()
# obj.getdata()
# obj.s_branch = "cs" # adding instance variable by using object
# print(obj.__dict__)
# print(obj.s_mb)
# del obj.roll           #delete a variable 
# print(obj.__dict__)


# - Static variable - is not dependent on the object --without using self variable --declared inside the class and not inside the constructor
# class College:
#     coll = "Sai Holy Faith"
#     def __init__(self):
#         self.name = "Vihas"

# principal = College()
# teacher = College()
# student = College()
# print(principal.coll," ",principal.name)
# print(teacher.coll," ",teacher.name)
# print(student.coll," ",student.name)

# College.coll = "Sai Holy Faith High School"
# principal.name = "Raj"

# print(principal.coll," ",principal.name)
# print(teacher.coll," ",teacher.name)
# print(student.coll," ",student.name)


# difference between static and instance variable

# where we can declare static variable?
# - inside the class but outisde of method

# class College:
#     coll = "Sai Holy Faith"
#     def __init__(self):
#         self.name = "Vihas"
#         College.clgid = 1234567
    
#     def getdata(self):             #instance method
#         College.add = "Vashi"
#         print(College.add)

# principal = College()
# teacher = College()
# student = College()
# print(principal.coll," ",principal.name,principal.clgid)
# print(teacher.coll," ",teacher.name,teacher.clgid)
# print(student.coll," ",student.name,student.clgid)

# principal.getdata()
# print("College var: ",College.add)
# teacher.getdata()
# student.getdata()

# College.coll = "Sai Holy Faith High School"
# College.clgid = 9876543
# College.add = "Koparkhairane"
# principal.name = "Raj"

# print(principal.coll," ",principal.name,principal.clgid)
# print(teacher.coll," ",teacher.name,teacher.clgid)
# print(student.coll," ",student.name,student.clgid)

# decorator: is used to modify the behaviour of function
# Static method
# class Student:
# #decorator
#     @staticmethod
#     def get_data(firname,lastname):          #static method --self keyword is not used
#         print("First Name: ",firname,"Last Name: ",lastname)
    
#     def contatc(mobile,roll):
#         print("your contact",mobile,roll)

# Student.get_data("Vihas","Poojari")
# Student.contatc(54345676543,1001)

# ================================================================================================================================

# Garbage collector
# garbage collector scans for the unused memory and it informs the destructor 
# destructor performs the clean up operation like closing the file or closing the connection then it informs the garbage collector
# then the gc deallocates the memory

# =================================================================================================================================
# single inheritance
# class A:
#     def coll_name(self):
#         print("Sai Holy Faith")
        
# class Student(A):
#     def coll_name(self):
#         super().coll_name()
#         print("Vihas")
        
# obj = Student()
# obj.coll_name()
# obj.student_info()

# ================================================================================================================================
# Multilevel inheritence
# class A:
#     def coll_name(self):
#         print("Sai Holy Faith")
        
# class Student(A):
#     def student_info(self):
#         print("Vihas")
        
# class Exam(Student):
#     def subject(self):
#         print("Subject1: Maths")
#         print("Subject2: English")
#         print("Subject3: Science")
        
# obj = Exam()
# obj.coll_name()
# obj.student_info()
# obj.subject()

# class SubMarks:
#     maths = int(input("Enter marks of maths: "))
#     de = int(input("Enter paper marks of de: "))
#     c= int(input("Enter paper marks of c: "))
#     eng = int(input("Enter paper marks of english: "))
    
# class PracMArks:
#     cparct = int(input("Enter paper marks of cparct: "))
    
# class Result(SubMarks,PracMArks):
#     def total(self):
#         if self.maths >= 40 and self.de >= 40 and self.c >= 40 and self.eng >= 40 and self.cparct >= 40:
#             print("pass")
#         else:
#             print("fail")
        
# obj = Result()
# obj.total()


# class A:
#     def add(self):
#         print("This is A class")

# class B():
#     def add(self):
#         print("This is B class")
        
# class C(A,B):
#     def add(self):
#         super().add()
#         print("This is C class")
        
# obj = C()
# obj.add()
    
# ================================================================================================================================


# Polymorphism
# - Compile time polymorphism  --eg. function overloading
# - Run time polymorphism      --eg. function overriding

# class Arithematic:
#     def add(self,a):
#         print(a)
        
#     def add(self,a,b):
#         print(a+b)
      
#     def add(self,a,b,c):
#         print(a+b+c)
        
# obj = Arithematic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)
# Error occurs in the  above code

# Hard coded to slove method overloading problem
# class Arithematics:
#     def add(self,a=None,b=None,c=None):
        
#         if a!= None and b!= None and c!= None:
#             print(a+b+c)
#         elif a!= None and b!= None:
#             print(a+b)
#         else:
#             print("Enter at least 2 numbers")
            
# obj = Arithematics()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# class A:
#     def __init__(self):
#         print("There is no arguments")
#     def __init__(self,a):
#         print("There is one arguments")
#     def __init__(self,a,b):
#         print("There are two arguments")
    
# obj = A()
# obj = A(10,20)
# obj = A(10)
# there is problem in the above code

# overriding
# overriding is only possible in parent child relationship
# class RBI:
#     def home_roi(self):
#         print("Home loan ROI: 7.5%")
        
#     def carLoan(self):
#         print("Car loan ROI: 8%")
        
# class SBI(RBI):
#     def home_roi(self):
#         print("Home loan ROI: 6.5%")
#         super().home_roi()                                   #super() is used to call the parent class method

# obj = SBI() 
# obj.home_roi()
# obj.carLoan()

# constructor overriding
# class Father:
#     def __init__(self):
#         print("Father: = i am already at breakfast table")
        
# class Child(Father):
#     def __init__(self):
#         super().__init__()
#         print("Child: = i will be late for breakfast")
        
# obj = Child()
        
# ================================================================================================================================
# Encapsulation






# Pattern
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end="")
#     print()
    
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+1-j,end="")
#     print()
    
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=" ")
#     print()

# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,end="")
#     print()

# import time
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# import time
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(i-i),end=" ")
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
#     print()



# def duplicate(n):
#     n=str(n)
#     a=set(n)
#     count=0
    
#     for i in a:
#         if n.count(i)>1:
#             count=count+1
            
#     if count>0:
#         return count
#     else:
#         return -1
        
# n=int(input("Enter the data: "))
# print(duplicate(n))

# ================================================================================================================================
# ABSTRACTION
# from abc import ABC,abstractmethod
# class Help4(ABC):
#     @abstractmethod
#     def training(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass
    
# class Ashish(Help4):
#     def training(self):
#         print("C , CPP , Java")
#     def placement(self):
#         print("Java Placement")
        
# class Anish(Help4):
#     def training(self):
#         print("Python | Django")
#     def placement(self):
#         print("Python Placement")
        
# class Aniket(Help4):
#     def training(self):
#         print("Machine Learning")        
#     def placement(self):
#         print("Data Science")
    
# obj = Anish()
# obj.training()
# obj.placement()