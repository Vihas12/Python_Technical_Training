import sys
class Node:
    #responsibility of this class is to create a node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    #add node 
    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    # display linked list
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
            
        
if __name__ == '__main__':
    object = LinkedList()
    while True:
        print("\n1.Add Song to List")
        print("2.Add Song in Beginning")
        print("3.Add Song at Between") 
        print("4.Add Node at End")
        print("5.Display Linked List")
        print("6.Exit")
        
        ch = int(input("Enter your choice: "))
        if ch == 1:
            value = input("Enter name of song: ")
            object.addNode(value)
            print("song added successfully")
        elif ch == 2:
            value = input("Enter name of song: ")
            object.addAtBegin(value)
            print("Song added successfully in the beginning")
        elif ch == 3:
            pass
        elif ch == 4:
            pass
        elif ch == 5:
            object.display()
        elif ch == 6:
            sys.exit()
        else:
            print("Invalid choice")
            