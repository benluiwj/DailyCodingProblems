# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the head of a singly linked list, swap every two nodes and return its
# head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
# Definition for singly-linked list.

from typing import *

"""

3 pts 

prev, curr, next

 [1 2 3 4]
  ^ ^ ^

swap prev and curr

set prev to next.next
set curr to next.next.next
set next to prev


if its a list

take 2 indexes and swap them pairwise


in a LL

head = head+1
head+1 = head

head+2 = head+3
head+3 = head+2


d 1 2 3 4
                                                                                                                               ^ ^ ^
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return head
        
        dummy = ListNode(next = head)
        prev = dummy
        curr = head
        next = head.next
        
        while curr and curr.next:
                curr.next = next.next
                prev.next = next
                next.next = curr
                
                if not curr.next:
                        break
                
                prev = curr
                curr = prev.next
                next = curr.next
        
        return dummy.next

root1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

sol = Solution().swapPairs(root1) 

while sol:
        print(sol.val)
        sol = sol.next