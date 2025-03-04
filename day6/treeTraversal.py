"""
Tree: 
                                                                    N1
                                                                  /   \
                                                                N2     N3
                                                              /   \   /  \
                                                            N4   N5  N6  N7
                                                           /  \
                                                         N8   N9
"""
# import QueueLinkedList as ql
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)
   
    
def preorder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder(rootNode.left)
    preorder(rootNode.right)
           
   
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
    
node1 = BinaryTree("N1")
node2 = BinaryTree("N2")
node3 = BinaryTree("N3")
node4 = BinaryTree("N4")
node5 = BinaryTree("N5")
node6 = BinaryTree("N6")
node7 = BinaryTree("N7")
node8 = BinaryTree("N8")
node9 = BinaryTree("N9")

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
node4.left=node8
node4.right=node9

print(node1)
inorder(node1)