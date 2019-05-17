import sys
x = sys.argv[1]
c = len(sys.argv[1:])
# Python program to for tree traversals 

  # A class that represents an individual node in a 
  # Binary Tree 
class Node: 
    def __init__(self,key): 
       self.left = None
       self.right = None
       self.val = key


def insert(root, node):
    if root is None:
        root =node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right =node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left =node
            else:
                 insert(root.left, node)

def printPreorder(root):
     if root: 
       print(root.val), 
       printPreorder(root.left) 
       printPreorder(root.right) 
root= Node(int(sys.argv[1]))
for i in range(c-1):
    insert(root,Node(int(sys.argv[i+2])))

printPreorder(root) 
