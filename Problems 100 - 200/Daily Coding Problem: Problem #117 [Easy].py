# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.
def least_sum(root):
        if not root:
                return 0
        
        lowest = root.val
        frontier = [root]
        
        while frontier:
                new_frontier = []
                total = 0
                for node in frontier:
                        if node.left:
                                total += node.left.val
                                new_frontier.append(node.left)       
                        
                        if node.right:
                                total += node.right.val
                                new_frontier.append(node.right)
                
                lowest = min(lowest, total)
                frontier = new_frontier
        
        return lowest