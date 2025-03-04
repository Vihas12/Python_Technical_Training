# f = open('day6/myfile.txt','w')
# print("name of file",f.name)
# print("file mode",f.mode)
# print("readable",f.readable())
# print("writeable",f.writable())
# print("file has closed",f.closed)
# f.close()

# perform write operation
# f=open("day6/myfile.txt",'a')
# f.write("Mumbai is a smart city\n")
# f.close()
# print("file operation is done")


# inserting list
# f=open("day6/myfile.txt",'a')
# myList = ["Prasad","Rahul","Ram","Suresh"]
# myTuple = ("Prasad","Rahul","Ram","Suresh")
# dic = {'a':1,'b':2}
# f.writelines(myList)
# f.writelines(myTuple)
# f.writelines(dic)
# f.close()
# print("written work has done succesfully")

#
# with open("day6/myfile.txt",'w') as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("file closed",f.closed)
# print("file is closed now: ",f.closed)

# file handling on image file
# f1 = open("day6/Sc.png",'rb')
# f2 = open("day6/Rs.png",'wb')
# data = f1.read()
# print(data)
# f2.write(data)
# print("image copied successfully")

# operation on csv file
# import csv
# f = open("day6/student.csv",'r',newline="")
# a = csv.writer(f)
# a.writerow(["studentID","rollno","name","mobileno"])
# nu = int(input("Enter how many student: "))
# for i in range(nu):
#     studentid = int(input("Enter student id: "))
#     rollno = int(input("Enter your roll no: "))
#     name = input("Enter your name: ")
#     mobile = int(input("Enter your mobile no: "))
#     a.writerow([studentid,rollno,name,mobile])
# read the csv
# r = csv.reader(f)
# for i in r:
#     print(i)

# Task
# import csv
# f = open("day6/student_detail.csv",'a',newline="")
# a = csv.writer(f)
# a.writerow(["SID","studentname","studenBranch",'p1','p2','p3','p4','p5','total','percentage','grade','result'])
# id = 0

#  name = input("Enter your name: ")
# branch = input("Enter your branch: ")
# p1 = int(input("Enter your p1: "))
# p2 = int(input("Enter your p2: "))
# p3 = int(input("Enter your p3: "))
# p4 = int(input("Enter your p4: "))
# p5 = int(input("Enter your p5: "))

# id += 1
# total = p1+p2+p3+p4+p5
# percen = (total/500)*100
# grade = ''
# res = ''
# if percen>80 and percen<=100:
#     grade = 'A'
# elif percen>60 and percen<=80:
#     grade = 'B'
# elif percen>50 and percen<=60:
#     grade = 'C'
# else:
#     grade = 'D' 
# if p1<40 or p2<40 or p3<40 or p4<40 or p5<40:
#     res = "Fail"
# else:
#     res = "Pass"
# a.writerow([id,name,branch,p1,p2,p3,p4,p5,total,percen,grade,res])
