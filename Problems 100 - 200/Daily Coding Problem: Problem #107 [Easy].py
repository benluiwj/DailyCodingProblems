# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Print the nodes in a binary tree level-wise. For example, the following should
# print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#    / \
#   4   5

def level_traversal(root):
        if not root:
                return
        
        frontier = [root]
        
        while frontier:
                new_frontier = []
                for node in frontier:
                        print(node.val)
                        if node.left:
                                new_frontier.append(node.left)
                        
                        if node.right:
                                new_frontier.append(node.right)
                
                frontier = new_frontier
                