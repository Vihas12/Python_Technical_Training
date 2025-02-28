name = "adhjsdhaflrhrlg"
print(name[::-1])

a=1
print(f"{a} is good boy")

name="Prashant"
print("{} is name of the man ".format(name))

s="Python is a programming language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

s="Vihas","Ravi","Poojari"
m=" | ".join(s)
print(m)

s="help4code is a best platform for practicing programming"
# returns first index of matching string
print(s.find("best")) 
# returns -1 if not found
print(s.find("dhsf")) 

print("shafgjwegr3473892479".isalnum())
print("shafgjwegr".isalpha())
print('7777f'.isdigit())
print("shafgjwegr".islower())
print(''.islower())
print("SDHGDSFSDF".isupper())
print('My name is Prashant'.istitle())
print("hello".startswith("He"))
print("hello".endswith("lo"))


print(int(3.14))
# complex cannot be converted to int
print(int(10+5j)) 
print(int(True))
# string with float cannot be converted to int
print(int("4.22"))
print(int("4"))


print(float(3))
# complex cannot be converted to float
print(float(10+5j))
print(float(True))
print(float("4.22"))
print(float("4"))

# every datatype can be converted to compolex
print(complex(3))
print(complex(12.5))
print(complex(5,-3))
print(complex(True,False))


# false for 0, " ", 0+0j
print(bool(0))  
print(bool(14))
print(bool(0.0))
print(bool(1.1))
print(bool(0+0j))
print(bool(""))
print(bool("hello"))

# membership operator --in --not in
# membership operator checks whether the elemnet is present in it or not
for i in range(5):
    print(i)
    
for i in range(1,10,2):
    print(i)


for i in range(1,11):
    print(i*1,"   ",i*2,"   ",i*3,"   ",i*4,"   ",i*5,"   ",i*6,"   ",i*7,"   ",i*8,"   ",i*9,"   ",i*10)
    
print("-------------------------------------------------------------------------------")
for i in range(1,11):
    print(i*11,"   ",i*12,"   ",i*13,"   ",i*14,"   ",i*15,"   ",i*16,"   ",i*17,"   ",i*18,"   ",i*19,"   ",i*20)
    
    

# identity operator --is --is not
# identity operator checks the address


# WAP to accept 5 paper marks and calculate total, percentage, if candidate pass 
# in all paper then he/she is pass else show fail passing marks is 40
# if percentage = 40 to 60 assign "C"
# if percentage = 60 to 80 assign "B"
# if percentage = 80 to 100 assign "A"
  
  
math1 = int(input("Enter marks of maths: ")) 
eng = int(input("Enter marks of english: "))
mara = int(input("Enter marks of marathi: ")) 
hindi = int(input("Enter marks of hindi: "))
sci = int(input("Enter marks of science: "))

if(math1<=40 or eng<=40 or mara<=40 or hindi<=40 or sci<=40):
    print("Student fails")
else:
    print("pass")
    
    total =math1 + eng + mara + hindi + sci
    percent = (total/500) * 100
    
    if(percent>40 and percent<=60):
        print("Grade: C")
    elif(percent>60 and percent<=80):
        print("Grade: B")
    elif(percent>80 and percent<=100):
        print("Grade: A")
    

# WAP to accept one character as input check and display inpu is 
# 1.upper case
# 2.lower case
# 3.digit
# 4.special smbol


ch = ord(input("Enter any single char: "))

if ch>=65 and ch<=91:
    print("Upper case")
elif ch>=97 and ch<=122:
    print("Lower case")
elif ch>=48 and ch<=57:
    print("digit")
else:
    print("Special char")
    

# zip() is a function used to take two range function together
# WAP to print the pattern
# 1 5
# 2 4
# 4 2
# 5 1

for i in range(1,6):
    if(i==3):
        continue
    print(i," ",6-i)
    
# using zip
for i,j in zip(range(1,6),range(5,0,-1)):
    if(i==3):
        continue
    print(i," ",j)


# arithmeic operaion
a=50
b=30
c=20
d=10

print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

# List 
rollno = [3,5,7,1,11,4,5,2]

for x in rollno:
    if x==2 or x==4 or x==6 or x==8:
        print("which even no is found ",x)
        break


cont = [2,1,4,5,5,4,4,1,1]
count = 0
even = 0
odd = 0

for i in cont:
    if i==4:
        count = count+1
    elif i==2:
        even = even + 1
    elif i==5:
        odd = odd + 1
        
print(count-even)
print(count-odd)

# palindrome
# without for loop
ch=input("Enter a string to check palindrome: ")
ch = ch.lower()
if ch == ch[::-1]:
    print("Is Palindrome")
else:
    print("Not palindrome")
    
    
# count the count of vowel and consonant
vow=['a','e','i','o','u']
cvow=0
ccon=0
ch=input("Enter a string: ")

for i in ch:
    if i in vow:
            cvow = cvow + 1 
    else:
            ccon = ccon + 1

print(cvow)
print(ccon)

# check anagram
ch1=input("Enter a string1: ")
ch2=input("Enter a string2: ")

if len(ch1) == len(ch2):
    sr1 = list(ch1)
    sr2 = list(ch2)
    
    sr1.sort()
    sr2.sort()

    if sr1 == sr2:
        print("Anagram")
    else:
        print("Not a anagram")
        
        

# check panagram(contains all letter in alphabet)
# input: "The quick brown fox jumps over the lazy dog"
# output: Panagram

alp='qweryuiopasdfghjklzxcvbnm'
alp=list(alp)
alp=alp.sort()


# remove duplicate elements
name=input("Enter a string1: ")
newsr=''

for i in name:
    if i not in newsr:
        newsr+=i
    
print(newsr)
        
# count substring in string
ch1=input("Enter a string1: ")
ch2=input("Enter a string2: ")

n=ch1.count(ch2)
print(n)

# count the words in string
ch1=input("Enter a string1: ")
sp=0
if(ch1 == ""):
    sp=0
else:    
    sp=1
    for i in ch1:
        if i==" ":
            sp=sp+1

print(sp)

# WAP to compress a string by replacing consecutive char with their count
# input: aaabbbccccc
# output: a3b4c4
ch1=input("Enter a string1: ")
a=''
l=[]
c=0

for i in ch1:
    if i not in a:
        a+=i

for i in a:
    c=i.count(ch1)
    l.append(c)
for i in range(len(a)):
    print(a[i],l[i],sep='',end='')
    
    
# given an array return an array where each elements is the product of all the elements in the array except itself
a=[1,2,3,4]
b=[]

for i in a:
    m=1
    for j in a:
        if i != j:
            m=i*j
    b.append[m]
    
print(b)