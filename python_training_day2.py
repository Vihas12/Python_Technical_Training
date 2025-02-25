# program of for with else
# mycart = [10,20,800,60,70]
# for i in mycart:
#     if i > 400:
#         print("This is no in my cart")
#         continue
    
#     print(i)
# else:
#     print("you have purchased everything")
    
    
# sum of natural numbers from 1 to 10 =55
# WAP to cal factorial of any number 5!=120
# 


# name = "Prashant"
# i=0
# for x in name:
#     if x == 'n':
#         print("The chraracter present at index no ",i,"value=:",x)  
#         break
#     i=i+1


# Error handling

"""
TYPES of error: 
    --compile time error (syntax error) - handled by developer and 
    --run time error    (exception) 
"""
# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# except ZeroDivisionError as msg:
#     print("cannot be divided by zero: ",msg)
# except ValueError as msg:
#     print("invalid input: ",msg)
    
"""
can multiple exception be handled in single except block?
--yes
"""

# handeling multiple errorrs in a single except block
# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
    
# default except block
# a default 'except' block should be at the last
# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# # default 'except:' must be last 
# # except:
# #     print("This is default except block")
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
# except:
#     print("This is default except block")

# using else with try and except
# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
# else:
#     print("Everything is OK")
    
"""
Enter first value: 5
Enter second value: 4
1.25
Everything is OK
"""

# using finally

# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
# finally:
#     print("This is executed every time")

"""
Enter first value: 5
Enter second value: @
invalid literal for int() with base 10: '@'
This is executed every time

Enter first value: 4
Enter second value: 5
0.8
This is executed every time
"""

# nested try and except block
# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))
#     try:
#         print(val1/val2)
#     except ZeroDivisionError as ms:
#         print(ms)
# except (ValueError) as msg:
#     print(msg)

# try:        
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))

#     print(val1/val2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
# else:                                                    # else block cannot come after finally block
#     print("Everything is OK")
# finally:
#     print("This is finally block")


"""
Logging 
If we want to store complete application flow and exception details in a file so we should use logging module
"""

# MCQ's
# a=[1,2,3,4,5,6,7,8,9] 
# a[::2]=10,20,30,40,50,60                #asn: ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# print(a)


# def fun(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# print(t,v[0])                          # ans: 3 44



# data = [[[1,2],[3,4]],[[5,6],[7,8]]]
# def fun(m):
#     v=m[0][0]
#     for row in m:
#         for e in row:
#             if v < e:v=e
#     return v

# print(fun(data[0]))                   # ans: 4



# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):                  # pop function pops the last element
    # print(arr[i].pop())               # ans: 4 7 11 15
    
    
# def f(i,value=[]):                     #value = [] is a default list
#     value.append(i)
#     print(value)
# f(1)                                   # [1]
# f(2)                                   # [1,2]
# f(3)                                   # [1,2,3]


# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end='')


# f1 = ['Apple','Berry','Cherry','Papaya']
# f2 = f1                                         #list alising f2 and f1 have the same address
# f3 = f1[:]
# f2[0] = 'Guava'                                 # f1 =  ['Guava','Berry','Cherry','Papaya']  and f2 =  ['Guava','Berry','Cherry','Papaya']
# f3[1] = 'Kiwi'                                  # f3 =  ['Apple','Kiwi','Cherry','Papaya']

# sum = 0
# for ls in (f1,f2,f3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)                                         # ans : 22




