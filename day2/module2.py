# first way of importing By module name we will access var, fun , class
# import module1

# module1.welcome("admin","pass")
# print(module1.pi)
# module1.square(5)


# second way of importing by alias name (short form) eg. m1
# import module1 as m1

# m1.welcome("admin","pass")
# print(m1.pi)
# m1.square(5)


# third way to import a specific fun/var/class etc
# from module1 import pi,square,login
# print(pi)
# square(5)
# login('user','user')


# fourth way to import everything
# from module1 import *
# print(pi)
# square(5)
# login('user','user')


# predefined modules
# import math
# print(math.sqrt(16))
# print(math.pi)

# from math import *
# print(int(sqrt(4)))
# print(ceil(3.6))
# print(floor(3.6))
# print(fabs(-3.6))
# print(fabs(3.6))

# from random import *
# for i in range(5):
#     print(randint(1,100000))

# from random import *
# for i in range(5):
#     print(random())

# from random import *
# for i in range(5):
#     print(uniform(1,10))

from random import *
list = ['prashant','rahul','ashish','vijay','sahil','nikhil']
for i in range(10):
    print(choice(list))