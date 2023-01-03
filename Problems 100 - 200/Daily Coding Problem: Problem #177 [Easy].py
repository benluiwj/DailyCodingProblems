# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a linked list and a positive integer k, rotate the list to the right by k 
# places.

# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 
# 3 -> 5 -> 7 -> 7.

# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4
# -> 5 -> 1 -> 2.
from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateLL(head):
    prev = None
    curr = head
    while curr.next:
        prev = curr
        curr = curr.next
    
    prev.next = None
    curr.next = head
    return curr
    

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        rotate = k % length
        new_head = head
        while rotate:
            new_head = rotateLL(new_head)
            rotate -= 1
        
        return new_head

        