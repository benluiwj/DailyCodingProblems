# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
# node with value 8.

# In this example, assume nodes with the same value are the exact same node
# objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and
# constant space.
from typing import List


class ListNode:
        def __init__(self, val = 0, next = None):
                self.val = val
                self.next = next

def getIntersectionNode(headA, headB):
        # get lengths of each
        
        lengthA = 0
        tempA = headA
        while tempA:
                lengthA += 1
                tempA = tempA.next
                
        lengthB = 0
        tempB = headB
        while tempB:
                lengthB += 1
                tempB = tempB.next
        
        # find difference
        
        diff = abs(lengthA - lengthB)
        
        # move longer one forward by diff
        
        tempA = headA
        tempB = headB
        if lengthA > lengthB:
                for _ in range(diff):
                        tempA = tempA.next
        
        else:
                for _ in range(diff):
                        tempB = tempB.next
        
        # traverse together
        
        for _ in range(min(lengthA, lengthB)):
                if tempA.val == tempB.val:
                        return tempA
                
                tempA = tempA.next 
                tempB = tempB.next 
        
        return None

[4,1,8,4,5]
[5,6,1,8,4,5]
a = ListNode(4, next = ListNode(1, next= ListNode(8)))
b = ListNode(5, next = ListNode(6, next = ListNode(1, next = ListNode(8))))

getIntersectionNode(a,b)