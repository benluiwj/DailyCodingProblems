# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a binary tree, return all paths from the root to leaves.

# For example, given the tree:

#    1
#   / \
#  2   3
#     / \
#    4   5


# Return [[1, 2], [1, 3, 4], [1, 3, 5]].

"""

DFS from the root

"""

class Node:
        def __init__(self, val = None, left = None, right = None):
                self.val = val
                self.left = left
                self.right = right

def paths_to_leaves(root):
        paths = []
        
        def helper(curr_path, node):
                if not node.left and not node.right:
                        paths.append(curr_path[::])
                        return
                
                if node.left:
                        curr_path.append(node.left.val)
                        helper(curr_path, node.left)
                        curr_path.pop()
                
                if node.right:
                        curr_path.append(node.right.val)
                        helper(curr_path, node.right)
                        curr_path.pop()
        
        helper([root], root)
        return paths
