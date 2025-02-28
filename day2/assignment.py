stdId = []
stdName = []
stdRollNo = []
stdCity = []

def add():
    try:
        id = int(input("Student Id: "))
        if id in stdId:
            print("Student ID already available")
            return
            
        rollNo = int(input("Student Roll No.: "))     
        if rollNo in stdRollNo:
            print("Student Roll No. already available")
            return
            
        name = input("Students Name: ") 
        if(name.isalpha() == False):
            print("Enter a valid Name")
            return
                   
        city = input("Student City: ")            
        if(city.isalpha() == False):
            print("Enter a valid City Name")
            return
        else:
            stdId.append(id)
            stdRollNo.append(rollNo)
            stdName.append(name)
            stdCity.append(city)
    except ValueError:
        print("Invalid Id or Roll No.")
    
def showdet():
    print("Student ID\tStudent Roll No.\tStudent Name\t\t\t\tStudent City")
    print("--------------------------------------------------------------------------------------------------")
    for i in range(len(stdId)):
        print(stdId[i],"\t\t",stdRollNo[i],"\t\t\t",stdName[i],"\t\t\t",stdCity[i])
        print("--------------------------------------------------------------------------------------------------")
    
def update():
    try:
        upn = int(input("Select Student ID: "))
        if upn in stdId:
            i=stdId.index(upn)
            print("1.Student Name: ",stdName[i])
            print("2.Student Roll No.: ",stdRollNo[i])
            print("3.Student City: ",stdCity[i])
            print("4.Return to the menu")
            c=int(input("Select the detail to update: "))
            if c==1:
                name = input("Students Name: ")
                if(name.isalpha() == False):
                    print("Enter a valid Name")
                else:
                    stdName[i]=name
            elif c ==2:
                rollNo = int(input("Student Roll No.: "))
                if rollNo.isalpha() == True:
                    print("Please enter a valid Student Roll No. ")
                else:
                    stdRollNo[i]=rollNo
            elif c == 3:
                city = input("Student City: ")
                if(city.isalpha() == False):
                    print("Enter a valid City Name")
                else:
                    stdCity[i]=city
            elif c == 4:
                return
            else: 
                print("Please select from the given option")
        else:
            print("Select an ID that exist")
    except ValueError:
        print("Please enter numbers")
                
def dele():
    try:
        upn = int(input("Select Student ID: "))
        if upn in stdId:
            i=stdId.index(upn)
            print("1.Student Name: ",stdName[i])
            print("2.Student Roll No.: ",stdRollNo[i])
            print("3.Student City: ",stdCity[i])
        
        cho = input("Are you sure you want to detele this detail (y/n): ")
        if cho == 'y':
            stdId.remove(stdId[i])
            stdCity.remove(stdCity[i])
            stdName.remove(stdName[i])
            stdRollNo.remove(stdRollNo[i])
        elif cho == 'n':
            return
        else:
            print("Enter a correct choice")
            return
    except:
        print("Please enter numbers")
    

while(True):
    print("\n1.Add student\n2.Show Students\n3.Update Details\n4.Delete Students")
    try:
        ch = int(input("\nSelect an operation: "))
        if ch == 1:
            add()
        elif ch == 2:
            showdet()
        elif ch == 3:
            update()
        elif ch == 4:
            dele()
        else:
            print("Please select from the given choice")
    except ValueError:
        print("Please select from the correct choice")
        
