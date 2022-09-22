# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a binary tree of integers, find the maximum path sum between two nodes.
# The path must go through at least one node, and does not need to go through the
# root.
# Definition for a binary tree node.

from typing import *

"""

compare left and right nodes 

see if its possible to combine to get a greater path. 3 possible combinations: L + C, L+C+R, R+C

if its a tree already, cannot form another path

alternatively if its not possible to combine, take the bigger of the left and right.

at each call to helper, return a tuple of bool and integer. bool will tell us whether the root node was included or not. integer would be the biggest sum.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
                if not node:
                        return float('-inf'), 0
                
                left_max, left_path = helper(root.left)
                right_max, right_path = helper(root.right)
                
                # max path through root
                root_max_sum = max(0, left_path) + root.val + max(0, right_path)
                
                # max path either with or without root
                max_sum = max(left_max, root_max_sum, right_max)
                
                # max path including and ending at root
                root_path = max(left_path, right_path, 0) + root.val
                
                return max_sum, root_path
        
        result, _ = helper(root)
        return result

sol = Solution()

# root1 = TreeNode(1, left= TreeNode(2), right= TreeNode(3))
# root2 = TreeNode(-10, left = TreeNode(9), right = TreeNode(20, left = TreeNode(15), right = TreeNode(7))) 
root3 = TreeNode(1, left = TreeNode(-2, left = TreeNode(1, left = TreeNode(-1)), right = TreeNode(3)), right = TreeNode(-3, left = TreeNode(2)))

sol.maxPathSum(root3)
                        