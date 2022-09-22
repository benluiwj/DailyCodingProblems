# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f


# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d

class TreeNode:
        def __init__(self, val=0, left=None, right= None):
                self.val = val
                self.left = left
                self.right = right
                
class Solution:
        def invertTree(self, root):
                if not root:
                        return
                
                root.left, root.right = root.right, root.left
                
                self.invertTree(root.left)
                self.invertTree(root.right)
                
                return root
        
        