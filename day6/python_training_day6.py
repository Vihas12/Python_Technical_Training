# a = "sadfhgjgb sadfhgjg"
# b = ''
# st = a.split(" ")
# for i, j in zip(st[0], st[1]):
#     if i == j:
#         continue
#     else:
#         b = i
#         break  # Add this line to break out of the loop
# print(b)

# MAx element in each row
# a=[[100,198,333,323],
#    [122,232,221,111],
#    [223,565,245,764]]

# for i in range(len(a)):
#     b=0
#     for j in range(len(a[i])):
#         if b<a[i][j]:
#             b=a[i][j]
#     print(b)

# r=int(input("Enter the number of rows:"))
# a=int(input("Enter the number of columns:"))
# m=[]
# for i in range(r):
#     matrix = []
#     for j in range(a):
#         c=int(input(f"Enter the element for {i} row and {j} column:"))
#         matrix.append(c)
#     m.append(matrix)
# print(m)

# WAP to move *
# input = prashant*is*a*good*programmer
# output = ****prashantisagoodprogrammer 

# a = "prashant*is*a*good*programmer"
# b=''
# for i in a:
#     if i == "*":
#         b = b + "*"
# for i in a:
#     if i.isalpha():
#        b=b+i
# print(b) 
     
# # or
# a = "prashant*is*a*good*programmer"
# b=''
# v=''
# for i in a:
#     if i != '*':
#         b = b + i
#     else:
#         v+=i
# print(v+b)