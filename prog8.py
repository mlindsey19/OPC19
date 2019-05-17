import sys
x = sys.argv[1]
# Python program to for tree traversals 

  # A class that represents an individual node in a 
  # Binary Tree 
class Node: 
	def __init__(self,key): 
	self.left = None
	self.right = None
	self.val = key 
        
  def printInorder(root): 	    
  	if root: 
	          # First recur on left child 
          printInorder(root.left) 
				    
           # then print the data of node 
          print(root.val), 
						      
             # now recur on right child 
          printInorder(root.right) 
								        
  # A function to do postorder tree traversal 
  def printPostorder(root): 
										      
       if root: 
											    
      # First recur on left child 
         printPostorder(root.left) 
														      
        # the recur on right child 
         printPostorder(root.right) 
																        
     # now print the data of node 
   print(root.val), 
		    
#A function to do preorder tree traversal 
  def printPreorder(root): 
																      
     if root: 
																	    
        # First print the data of node 
       print(root.val), 
																	      
      
       printPreorder(root.left) 

																			       printPreorder(root.right) 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
print "Preorder traversal of binary tree is"
printPreorder(root) 
																				      
print "\nInorder traversal of binary tree is"
printInorder(root) 															
print "\nPostorder traversal of binary tree is"
printPostorder(root)

for c in x:
    if c in vowel:
        i = vowel.index(c)
        out += vowel[(i+1)%vv]
    elif c in cons:
        i = cons.index(c)
        out += cons[(i+1)%cc]
    else:
        e=1
if (e):
    print 'ERROR'
else:
    print out
