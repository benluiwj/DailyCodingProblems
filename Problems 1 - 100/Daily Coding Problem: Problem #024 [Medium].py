# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Implement locking in a binary tree. A binary tree node can be locked or unlocked
# only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

#  * is_locked, which returns whether the node is locked
#  * lock, which attempts to lock the node. If it cannot be locked, then it should
#    return false. Otherwise, it should lock it and return true.
#  * unlock, which unlocks the node. If it cannot be unlocked, then it should
#    return false. Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would
# like. You may assume the class is used in a single-threaded program, so there is
# no need for actual locks or mutexes. Each method should run in O(h), where h is
# the height of the tree.

class Node:
        def __init__(self, val = 0, left = None, right = None, parent = None, is_locked = False):
                self.val = val
                self.left = left
                self.right = right
                self.parent = parent
                self.is_locked = is_locked
                
                # following property reduces time from O(m+h) to O(h),
                # where m is number of nodes
                # no longer need to traverse entire tree, just traverse descendents 
                self.is_locked_descendent_count = 0 
        
        def is_locked(self):
                return self.is_locked
        
        def lock(self):
                if not self.is_ancestor_locked():
                        self.is_locked = True
                        
                        current = self.parent
                        while current:
                                current.is_locked_descendent_count += 1
                                current = current.parent
                        return True
                
                return False
        
        def unlock(self):
                if not self.is_ancestor_locked() :
                        self.is_locked = True
                        while current:
                                current.is_locked_descendent_count += 1
                                current = current.parent
                                
                        return True
                
                return False
        
        def is_ancestor_locked(self):
                parent = self.parent
                while parent:
                        if parent.is_locked():
                                return True
                        parent = parent.parent
                        
                return False
        
        
        
                                
                
                        
                