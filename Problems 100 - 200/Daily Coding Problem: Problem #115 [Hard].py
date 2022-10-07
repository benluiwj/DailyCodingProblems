# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two non-empty binary trees s and t, check whether tree t has exactly the
# same structure and node values with a subtree of s. A subtree of s is a tree
# consists of a node in s and all of this node's descendants. The tree s could
# also be considered as a subtree of itself.

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
                if not node1 and not node2:
                        return True
                
                if not node1 or not node2:
                        return False
                
                if node1.val == node2.val:
                    return helper(node1.left, node2.left) and helper(node1.right, node2.right)
                
                return False
        
        if not root:
            return False
        
        if helper(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)