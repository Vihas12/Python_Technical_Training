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
            
    # add node at beginning
    def addAtBegin(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node    
    
    
    # add node at between
    def addAtBetween(self,value,place):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif place == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for i in range(place-1):
                current = current.next
            node.next = current.next
            current.next = node
    
    
    def addAtEnd(self, value):
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
            print(current.data,"-->",end=" ")
            current = current.next
            
        
if __name__ == '__main__':
    object = LinkedList()
    while True:
        print("\n1.Add Node to Linked List")
        print("2.Add Node in Beginning")
        print("3.Add Node at Between") 
        print("4.Add Node at End")
        print("5.Display Linked List")
        print("6.Exit")
        
        ch = int(input("Enter your choice: "))
        if ch == 1:
            value = int(input("Enter value: "))
            object.addNode(value)
            print("Node added successfully")
        elif ch == 2:
            value = int(input("Enter value: "))
            object.addAtBegin(value)
            print("Node added successfully in the beginning")
        elif ch == 3:
            pl = int(input("Enter the position: "))
            value = int(input("Enter value: "))
            object.addAtBetween(value,pl)
            print("Node added successfully in the between")
        elif ch == 4:
            value = int(input("Enter value: "))
            object.addAtEnd(value)
            print("Node added successfully in the end")
        elif ch == 5:
            object.display()
        elif ch == 6:
            sys.exit()
        else:
            print("Invalid choice")
            