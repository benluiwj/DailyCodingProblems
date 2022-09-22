# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of numbers and an index i, return the index of the nearest larger
# number of the number at index i, where distance is measured in array indices.

# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

# If two distances to larger numbers are the equal, then return any one of them.
# If the array at i doesn't have a nearest larger integer, then return null.

# Follow-up: If you can preprocess the array, can you do this in constant time?

"""

at particular index, go forward to see what the biggest and return the distance
go backward to see the longest. compare the distances.

"""

def nearest_larger_integer(nums, index):
        biggest_right = float('inf')
        biggest_left = float('inf')
        n = len(nums)
        
        for i in range(index+1, n):
                if nums[i] > nums[index]:
                        biggest_right = i - index
                        break
        
        for i in range(index - 1, -1, -1):
                if nums[i] > nums[index]:
                        biggest_left = index - i
                        break
                
        if biggest_left > biggest_right:
                return index - biggest_left
        
        else:
                return index + biggest_right
        
        