# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Given a tree, find the largest tree/subtree that is a BST.

# Given a tree, return the size of the largest tree/subtree that is a BST.

# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

if the subtree is a bst, return true and the number of nodes as well. 

if left is bst and right is bst but entire tree isnt bst, then return taller of left and right

if only one is bst, then just return one. cos if other isnt bst, then overall wont be bst


   10
   / \
  5  15
 / \   \
1   8   7


at leaves -> True, 1

"""


class Solution:
    def largestBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return True, 0
            
            # handle leaves
            if not node.left and not node.right:
                return True, 1
            
            left_bst, left_nodes = helper(node.left)
            right_bst, right_nodes = helper(node.right)
            
            # if both are bst, return true and sum all the nodes + 1
            if left_bst and right_bst:
                if not node.left:
                    if node.right.val > node.val:
                        return True, right_nodes + 1
                    
                    else:
                        return False, right_nodes
                
                elif not node.right:
                    if node.left.val < node.val:
                        return True, left_nodes + 1
                    
                    else:
                        return False, left_nodes
                
                
                if node.left.val < node.val and node.right.val > node.val:
                    return True, left_nodes + right_nodes + 1
                
                else:
                    return False, max(left_nodes, right_nodes)
            
            # if either is bst but one isnt, then we should take the max of the left and the right, and since the tree itself is no longer a bst, return false
            return False, max(left_nodes, right_nodes)
        
        _, res = helper(root)
        return res

sol = Solution()

root = TreeNode(10, left = TreeNode(5, left = TreeNode(1), right = TreeNode(8)), right = TreeNode(15, right = TreeNode(7)))

print(sol.largestBST(root))
            