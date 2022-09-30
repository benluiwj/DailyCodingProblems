# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Determine whether a doubly linked list is a palindrome. What if it’s singly
# linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *

"""

reverse the linked list then iterate through to see if they are the same or not. once pass the middle can return already.

"""

class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:
                if not head or not head.next:
                        return True
                
                lst = []
                
                temp = head
                
                while temp:
                        lst.append(temp.val)
                        temp = temp.next
                        
                return lst == lst[::-1]