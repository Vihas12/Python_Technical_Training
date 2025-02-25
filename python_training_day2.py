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

