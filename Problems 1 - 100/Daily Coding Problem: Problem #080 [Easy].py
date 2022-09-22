# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root of a binary tree, return a deepest node. For example, in the
# following tree, return d.

#     a
#    / \
#   b   c
#  /
# d
class Node:
        def __init__(self, val = 0, left = None, right = None):
                self.val = val
                self.left = left
                self.right = right

def deepest_node(root):
        def helper(root):
                if not root:
                        return root, 1
                
                if not root.left and not root.right:
                        return root, 1
                
                
                left, left_depth = helper(root.left)
                right, right_depth =  helper(root.right)
                
                if left and not right:
                        return left, left_depth + 1
                
                if right and not left:
                        return right, right_depth + 1
                
                if left_depth < right_depth:
                        return right, right_depth + 1
                
                return left, left_depth + 1
        
        node, _ = helper(root)
        return node.val

root = Node(1, left = Node(2, left = Node(3)), right = Node(4))

print(deepest_node(root))
        