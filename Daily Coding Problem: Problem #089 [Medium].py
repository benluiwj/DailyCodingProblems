# Good morning! Here's your coding interview problem for today.

# This problem was asked by LinkedIn.

# Determine whether a tree is a valid binary search tree.

# A binary search tree is a tree with two children, left and right, and satisfies
# the constraint that the key in the left child must be less than or equal to the
# root and the key in the right child must be greater than or equal to the root.

from typing import *

# Definition for a binary tree node.

"""

traverse the tree in order and see if its sorted ascending. Otherwise its not valid.

another way is to compare the values with the root node.

if the left and right values are valid binary trees and they fulfil the bst property then its a binary tree

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
            
        in_order = []
        def traversal(node):
            if not node:
                return
            
            traversal(node.left)
            in_order.append(node)
            traversal(node.right)
        
        traversal(root)
        
        for i, node in enumerate(in_order):
            if i == 0:
                continue
            
            prev = in_order[i-1]
            if node.val < prev.val:
                return False
        
        return True
            
            