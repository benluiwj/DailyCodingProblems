# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from
# the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

"""
Without constrain for time, we can do the following:
1) iterate through to get the length
2) iterate through again until we reach the kth last element
3) delete it

Pointer which is k infront of the other. Once that pointer reached the end
pointer behind is at kth last. Perform removal.
"""


from typing import *

class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                end_pter = head
                count = 0
                while count < n:
                        if not end_pter:
                                break
                        end_pter = end_pter.next
                        count += 1
                
                if not end_pter:
                        head = head.next
                        return head
                
                prev = None
                start = head
                while end_pter:
                        end_pter = end_pter.next
                        prev = start
                        start = start.next
                
                prev.next = start.next
                
                return head

                              