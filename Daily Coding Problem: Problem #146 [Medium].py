# Good morning! Here's your coding interview problem for today.

# This question was asked by BufferBox.

# Given a binary tree where all nodes are either 0 or 1, prune the tree so that
# subtrees containing all 0s are removed.

# For example, given the following tree:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0


# should be pruned to:

#    0
#   / \
#  1   0
#     /
#    1


# We do not remove the tree at the root or its left child because it still has a 1 
# as a descendant.

"""

if the root is none, it can be removed

check left and right to see if they are removable ie no 1s in the subtree

if there is no ones, can remove



"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
                if not root:
                        return True
                
                left_prunable = helper(root.left)
                right_prunable = helper(root.right)
                
                # if left is prunable, prune left
                if left_prunable:
                        root.left = None
                
                # if right is prunable, prune right
                if right_prunable:
                        root.right = None
                
                
                return root.val == 0 and left_prunable and right_prunable
        
        helper(root)
        return root

sol = Solution()

root = TreeNode(0, left = TreeNode(1), right = TreeNode(0, left = TreeNode(1, left = TreeNode(0), right = TreeNode(0)), right = TreeNode(0)))

sol.pruneTree(root)


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0
