# simple implementation of linked list
# linked list is a data structure that contains a sequence of elements such that each element links to the next element in the sequence
class Node:
    #responsibility of this class is to create a node
    def __init__(self, value):
        self.item = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
linkObj = LinkedList()
linkObj.head = Node(10)
second = Node(20)
third = Node(30)

# connect nodes
linkObj.head.next = second
second.next = third

while linkObj.head is not None:
    print(linkObj.head.item,'--> ',linkObj.head.next,end=" ")
    linkObj.head = linkObj.head.next