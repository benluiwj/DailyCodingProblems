# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the head of a singly linked list, reverse it in-place.

from typing import *

"""

1->2->3 should become 3->2->1

3 pters

prev, curr, next

  v     v
[None 1 2 3]
      ^

curr.next = prev

prev = curr
curr = next
next = next.next



get the next variable of curr as temp or sth

then set curr.next = prev
shift set prev to be curr
and curr as temp

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return head
        
        prev = None
        curr = head
        next = head.next
        
        while next:
                curr.next = prev
                prev = curr
                curr = next
                next = next.next
        
        curr.next = prev
        return curr

sol = Solution()
temp = ListNode(val = 1, next = ListNode(2, next = ListNode(3)))
res = sol.reverseList(temp)

while res:
        print(res.val)
        res = res.next

