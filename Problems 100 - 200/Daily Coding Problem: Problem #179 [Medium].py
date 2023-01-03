# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the sequence of keys visited by a postorder traversal of a binary search
# tree, reconstruct the tree.

# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the
# following tree:

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

from typing import * 

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(order):
        if not order:
                return
        
        root = TreeNode(val=order[-1])
        index = len(order) - 1
        for i in range(len(order)-1):
                if order[i] > root.val:
                        index = i
                        break
        
        root.left = helper(order[:index])
        root.right = helper(order[index:-1])
        return root

class Solution:
    def constructFromPost(self, postorder: List[int]) -> Optional[TreeNode]:
            return helper(postorder)
    
sol = Solution()
sol.constructFromPost([2, 4, 3, 8, 7, 5])