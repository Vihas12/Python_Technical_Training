class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.children = []
        
    def __str__(self,level = 0):
        ret = " "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, treeNode):
        self.children.append(treeNode)
        
node1 = BinaryTree("Drinks")
node2 = BinaryTree("Hot")
node3 = BinaryTree("Cold")
node4 = BinaryTree("Tea")
node5 = BinaryTree("Coffee")
node6 = BinaryTree("Milk")
node7 = BinaryTree("Water")

node1.addChild(node2)
node1.addChild(node3)
node2.addChild(node4)
node2.addChild(node5)
node3.addChild(node6)
node3.addChild(node7)

print(node1)