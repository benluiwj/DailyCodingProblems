# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5,
# 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating
# a copy of the list. How many swap or move operations do you need?

"""

rotate array without creating a copy of the list.


"""

def rotate_arr_by_k(arr, k):
        for i in range(k, len(arr)):
                arr[i-k], arr[i] = arr[i], arr[i-k]
        
        return arr

rotate_arr_by_k([1,2,3,4,5,6], 2)