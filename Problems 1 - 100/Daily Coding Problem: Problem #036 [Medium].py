# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the
# tree.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
 10
 /
5

return 5

 10
 /
5
 \
  7
  
return 7

10
 \
  11

return 10

10
 \
  15
  /
12

return 12

10
 \
  15
  \
   17

return 15

Find successor of largest

2 cases :
largest has left child -> return largest from left child
largest has no child -> return parent


if node has right child -> go right and find largest

if node has no right child -> current node is largest -> find largest from left child

if node has no child -> return parent


perform reversed in-order traversal: right ->  root -> left
keep counter, when reach 2 jus return the node

"""             

def findSecondLargest(root):
        def inorder(root):
                if not root or count[0] == 2:
                        return
                
                if root.right:
                        inorder(root.right)
                
                count[0] += 1
                
                if count[0] == 2:
                        result.append(root)
                        return
                
                if root.left:
                        inorder(root.left)
        
        count = [0]
        result = []
        inorder(root)
        return result[0]
        

root1 = Node(10, left = Node(5))
root2 = Node(10, left = Node(5, right = Node(7)))
root3 = Node(10, right = Node(12, left = Node(11)))
print(findSecondLargest(root1).val)
print(findSecondLargest(root2).val)
print(findSecondLargest(root3).val)