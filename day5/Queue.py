# Queue operation

# 1.Enqueue
# 2.deQueue
# 3.Peek
# 4.isEmpty
# 5.isFull
# 6.Delete
# 7.Display
# 8.Exit

class Queue:
    def __init__(self,size):
        self.queueList = []
        self.size = size
        
    # isFull operation
    def isFull(self):
        if len(self.queueList) == self.size:
            return True
        else:
            return False
        
    # Push operation
    def enqueue(self):
        if self.isFull():
            print("The queue is full")
        else:
            self.value = int(input("Enter the element to push to queue: "))
            self.queueList.append(self.value)
        
    # Pop operation
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queueList.pop(0))
            
    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("Last elementof stack is ",self.queueList[0])
        
    # isEmpty operation
    def isEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False
        
    # Delete operation
    def deleteQueue(self):
        self.queueList = []
        print("Queue is deleted")
        
    # Display operation
    def display(self):
        print(self.queueList)
        
size = int(input("Enter the size of the queue: "))
obj = Queue(size)    
print("Queue has been created")

while True:
    print("\n1.Enqueue Operation: ")
    print("2.Dequeue Operation: ")
    print("3.Peek Operation: ")
    print("4.isEmpty Operation: ")
    print("5.isFull Operation")
    print("6.Delete Operation: ")
    print("7.Display Operation: ")
    print("8.Exit Operation: ")
    
    ch=int(input("Enter your choice: "))

    if ch == 1:
        obj.enqueue()
    elif ch == 2:
        obj.dequeue()
    elif ch == 3:
        obj.peek()
    elif ch == 4:
        print(obj.isEmpty())
    elif ch == 5:
        print(obj.isFull())
    elif ch == 6:
        obj.deleteQueue()        
    elif ch == 7:
        obj.display()
    elif ch == 8:
        break
    else:
        print("Enter a valid choice")
