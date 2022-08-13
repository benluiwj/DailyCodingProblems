# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given pre-order and in-order traversals of a binary tree, write a function to
# reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

# Definition for a binary tree node.

from typing import *

"""

preorder: root -> left -> right
inorder: left -> root -> right

from preorder, get value of root

find the index of the root in inorder. array to the left is left subtree array to right is right subtree

preorder :[a, b, d, e, c, f, g]

inorder :[d, b, e, a, f, c, g]
                   ^
                   
index = 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        if not preorder and not inorder:
            return
        
        root.val = preorder[0]
        
        index = -1
        
        for i, node in enumerate(inorder):
            if node == root.val:
                index = i
                break
        
        root.left = self.buildTree(preorder[1: index + 1], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
        
        return root

sol = Solution()

root = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])

print(root)