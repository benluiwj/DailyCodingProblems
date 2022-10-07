# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in
# the tree. Assume that each node in the tree also has a pointer to its parent.

# According to the definition of LCA on Wikipedia
# [https://en.wikipedia.org/wiki/Lowest_common_ancestor]: “The lowest common
# ancestor is defined between two nodes v and w as the lowest node in T that has
# both v and w as descendants (where we allow a node to be a descendant of
# itself).”

"""

if each node have pointer to parents, then just traverse upwards towards the root
keep a set of visited nodes

"""
def LCA(root, p, q):
        visited = {p, q}
        
        while p and q:
                parent_p = p.parent
                parent_q = q.parent
                if parent_p in visited:
                        return parent_p
                if parent_q in visited:
                        return parent_q
                
                visited.add(parent_p)
                visited.add(parent_q)
                p = parent_p
                q = parent_q
        
        return root
                        