# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given k sorted singly linked lists, write a function to merge all the lists into
# one sorted singly linked list.

"""

maintain the nodes in a min-heap. pop the top, add it to the new linked list and let it go next

can this be done in constant space??



"""

from typing import *
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for node in lists:
                heapq.heappush(node)
        
        result = ListNode()
        temp = result
        while heap:
                smallest = heapq.heappop()
                temp.next = ListNode(smallest.val)
                temp = temp.next
                move_smallest = smallest.next
                heapq.heappush(move_smallest)
        
        return result.next