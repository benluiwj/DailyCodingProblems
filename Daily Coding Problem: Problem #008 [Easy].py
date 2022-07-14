# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    1
#   / \
#  1   2
#     / \
#    2   2
#   / \
#  1   1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival(root):
        
        def helper(root):
                if not root.left and not root.right:
                        return 1, True
                
                
                left_count, is_left_unival = helper(root.left)
                right_count, is_right_unival = helper(root.right)
                is_same_val_as_root = root.left.val == root.val and root.right.val == root.val
                if not is_same_val_as_root:
                        return left_count + right_count, False
                
                else:
                        if is_left_unival and is_right_unival:
                                return 1 + left_count + right_count, True
                        
                        return left_count + right_count, False
        
        count, _ = helper(root)
        return count

root = TreeNode()

print(count_unival(root))