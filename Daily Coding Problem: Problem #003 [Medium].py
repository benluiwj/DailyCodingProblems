# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the
# tree into a string, and deserialize(s), which deserializes the string back into
# the tree.

# For example, given the following Node class

class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def serialize(root):
        token = "#"
        if not root:
                return token 
        
        return str(root.val) +  " " + serialize(root.left) + " " + serialize(root.right)
        

def deserialize(data):
        token = "#"
        if data == token :
                return Node(None)
        
        data = data.split()
        
        def helper(data, index):
                root_val = data[index]
                if root_val == token:
                        return None, index
                
                root = Node(root_val)
                root.left, next_index = helper(data, index + 1)
                root.right, last_index = helper(data, next_index + 1)
                return root, last_index
        
        res, _ =  helper(data, 0)
        return res
                
                
        
        


        


# The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

