# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Let's represent an integer in a linked list format by having each node represent
# a digit in the number. The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5


# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list
# format.

# For example, given

# 9 -> 9


# 5 -> 2


# return 124 (99 + 25) as:

# 4 -> 2 -> 1

class Node:
        def __init__(self, val=None, next=None):
                self.val = val
                self.next = next

def sum_linked_list(l1, l2):
        multiplier = 0
        l1_num = 0
        l2_num = 0
        
        temp = l1
        while temp:
                l1_num += temp.val * (10 ** multiplier)
                multiplier += 1
                temp = temp.next
        
        multiplier = 0
        temp = l2
        while temp:
                l2_num += temp.val * (10 ** multiplier)
                multiplier += 1
                temp = temp.next
        
        total = l1_num + l2_num
        result = Node()
        temp = result
        while total:
                node = Node(val = total % 10)
                total = total // 10
                temp.next = node
                temp = temp.next
        
        return result.next