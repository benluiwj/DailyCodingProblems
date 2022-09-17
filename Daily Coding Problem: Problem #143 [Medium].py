# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a pivot x, and a list lst, partition the list into three parts.

#  * The first part contains all elements in lst that are less than x
#  * The second part contains all elements in lst that are equal to x
#  * The third part contains all elements in lst that are larger than x

# Ordering within a part can be arbitrary.

# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may
# be [9, 3, 5, 10, 10, 12, 14].

"""

maintain 3 sections of the array, and perform swaps when appropriate

pivot is 10
            v
n 9 3 5 10 10 14 12 
      ^
           ^              

3 pters, low, curr, high

invariant is that the low pter has elements that are lower than pivot
high contains elements that are higher than pivot



"""


def three_way_partition(pivot, lst):
        low = -1
        curr = 0
        high = len(lst) - 1
        
        while curr <= high:
                if lst[curr] < pivot:
                        low += 1
                        lst[low], lst[curr] = lst[curr], lst[low]
                        curr += 1
                
                elif lst[curr] > high:
                        lst[high], lst[curr] = lst[curr], lst[high]
                        curr += 1
                        high -= 1
                
                else:
                        curr += 1
                        
                        