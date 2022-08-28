# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a linked list, sort it in O(n log n) time and constant space.

# For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99
# .

# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
"""

one way to do this is to get all values of the nodes into a list, sort the list and create new nodes. This would require O(n) space.
another O(n) space solution would be to map the nodes into a table, create a list like above and then reassign the pters of the nodes

for a O(1) solution, the only way would be to sort the nodes by rearranging the pters of the nodes.

base case would be to sort a linked list of length 2.

3 -> 2

to do this just reverse the pters to obtain 2 -> 3

suppose the original linked list is 3->2->1->4

the first sorted half will be 2->3 and the second half would be 1->4

to create the sorted list, have 2 pters to traverse both list

if the value of the first pter is greater than the second,

the first pter's next node would be the second pter

"""


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next:
            return head
        
        # split into 2 ll
        split = 0
        temp = head
        
        while temp:
            temp = temp.next
            split += 1
        
        middle = split // 2
        
        temp = head
        prev = None
        while middle > 0:
            prev = temp
            temp = temp.next
            middle -= 1
        
        list2 = temp
        prev.next = None
        list1 = head
        
        result1 = self.sortList(list1)
        result2 = self.sortList(list2)
        
        # merge
        
        return self.merge(result1, result2)
        
    
    def merge(self, head1, head2):
        if not head1:
            return head2
        
        elif not head2:
            return head1
        
        temp1 = head1
        temp2 = head2
        result = ListNode()
        tempResult = result
        while temp1 or temp2:
            if not temp1:
                tempResult.next = temp2
                break
            
            elif not temp2:
                tempResult.next = temp1
                break
            
            val1 = temp1.val
            val2 = temp2.val
            
            if val1 < val2:
                tempResult.next = temp1
                temp1 = temp1.next
                tempResult = tempResult.next
            
            else :
                tempResult.next = temp2
                temp2 = temp2.next
                tempResult = tempResult.next

        return result.next
        
sol = Solution()

ll = ListNode(3, next = ListNode(2, next = ListNode(1, next = ListNode(4))))

res = sol.sortList(ll)

res

while ll:
    print(ll.val)
    ll = ll.next

        
        