# Q.1
# def cal(m,n):
#     dif=0
#     sum1=0
#     sum2=0
#     for i in range(1,n+1):
#         if i%m == 0:
#             sum1 += i
#         else:
#             sum2 += i
#     return sum2-sum1
    

# res = cal(6,30)
# print(res)

# Q.2  ----WAP to calculate distance between 3 points
# x1=1 y1=1
# x2=2 y2=4
# x3=3 y3=6 

# from math import sqrt
# x1=1
# y1=1
# x2=2
# y2=4
# x3=3
# y3=6 
# d1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
# d2 = sqrt((x3 - x1)**2 + (y3 - y1)**2)
# d3 = sqrt((x3 - x2)**2 + (y3 - y2)**2)

# print(d1," ",d2," ",d3)

# Q3. factors of given no.
# def factors(num):
#     if num == 0:
#         print("No Factor")
#         return
#     if num < 0:
#         num = num * -1
#     lis = []
#     print(f"Factors of {num} are:",end=" ")
#     for i in range(1,num+1):
#         if num%i == 0:
#            print(i,end=" ")

# inp = int(input("Enter positive number: "))
# factors(inp)
n=69675
a = (n*n) + ((n-1)*(n-1));
print(a)        