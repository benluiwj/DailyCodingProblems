# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# We can determine how "out of order" an array A is by counting the number of
# inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] 
# but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than
# O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has
# three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten
# inversions: every distinct pair forms an inversion.

"""

naively -> follow what the question says. This can be done in O(n^2).

to do better, perform something like merge sort whilst counting the inversions. the key here is how to count the inversions.

to count the inversions between 2 sorted arrays say left (contain smaller elements) and right (contain bigger element):

initialise 2 pters
iterate through both arrays

if an element in left is greater than right,then the element in right is inverted with everything in the left since both are sorted.

[2 4] [1 3]

since 2 is greater than 1, this means that 1 is inverted with everything on the left ie 2 and 4. so we increase the count by 2.
"""


def count_and_sort(nums):
        if len(nums) <= 1:
                return 0, nums
        
        mid = len(nums) // 2
        left_count, left_sorted = count_and_sort(nums[:mid])
        right_count, right_sorted = count_and_sort(nums[mid:])
        
        i = 0
        j = 0
        
        count = 0
        result = []
        
        while i < len(left_sorted) and j < len(right_sorted):
                if left_sorted[i] > right_sorted[j]:
                        count += len(left_sorted) - i
                        result.append(right_sorted[j])       
                        j += 1
                
                elif left_sorted[i] < right_sorted[j]:
                        result.append(left_sorted[i])
                        i += 1
                
                else:
                        result.append(left_sorted[i])
                        result.append(right_sorted[j])
                        j += 1
                        i += 1
        
        if i == mid:
                result.extend(right_sorted[j:])
        
        else:
                result.extend(left_sorted[i:])
        
        return count + left_count + right_count, result


def count_inversions(nums):
        result, _  = count_and_sort(nums)
        print(result)
        return result

count_inversions([4,2,3,1])