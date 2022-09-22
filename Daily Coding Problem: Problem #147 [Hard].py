# Good morning! Here's your coding interview problem for today.

# Given a list, sort it using this method: reverse(lst, i, j), which reverses lst 
# from i to j.

"""
find the biggest element and its index then reverse it

"""


def reverse(lst, i, j):
        return lst[i:j:-1]

def my_sort(lst):
        
        def helper(lst, end_index):
                if end_index == 0:
                        return 
                biggest = float('-inf')
                index = -1
                for i, num in range(end_index):
                        if num > biggest:
                                biggest = num
                                index = i
                
                reverse(lst, index, end_index)
                helper(lst, end_index - 1)
        
        helper(lst, len(lst))