import sys
# Stack implementstion without size
# 1.Push
# 2.Pop
# 3.Peek
# 4.isEmpty
# 5.isFull
# 6.Delete stack
# 7.Display
# 8.Exit

class Stack:
    def __init__(self,size):
        self.stackList = []   #list representing stack
        self.size = size
        
    # isFull operation
    def isFull(self):
        if len(self.stackList) == self.size:
            return True
        else:
            return False
        
    # Push operation
    def push(self):
        if self.isFull():
            print("The stack is full")
        else:
            self.value = int(input("Enter the element to push to stack: "))
            self.stackList.append(self.value)
        
    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stackList.pop())
            
    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("Last elementof stack is ",self.stackList[-1])
        
    # isEmpty operation
    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False
        
    # Delete operation
    def deleteStack(self):
        self.stackList = []
        print("Stack is deleted")
        
    # Display operation
    def display(self):
        print(self.stackList)
        
size = int(input("Enter the size of the stack: "))
obj = Stack(size)    
print("Stack has been created")

while True:
    print("\n1.Push Operation: ")
    print("2.Pop Operation: ")
    print("3.Peek Operation: ")
    print("4.isEmpty Operation: ")
    print("5.isFull Operation")
    print("6.Delete Operation: ")
    print("7.Display Operation: ")
    print("8.Exit Operation: ")
    
    ch=int(input("Enter your choice: "))

    if ch == 1:
        obj.push()
    elif ch == 2:
        obj.pop()
    elif ch == 3:
        obj.peek()
    elif ch == 4:
        print(obj.isEmpty())
    elif ch == 5:
        print(obj.isFull())
    elif ch == 6:
        obj.deleteStack()        
    elif ch == 7:
        obj.display()
    elif ch == 8:
        # break
        # OR
        sys.exit()
    else:
        print("Enter a valid choice")
