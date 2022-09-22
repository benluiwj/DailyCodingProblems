# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7,
# 8, 8], since:

#  * 10 = max(10, 5, 2)
#  * 7 = max(5, 2, 7)
#  * 8 = max(2, 7, 8)
#  * 8 = max(7, 8, 7)

# Do this in O(n) time and O(k) space. You can modify the input array in-place and
# you do not need to store the results. You can simply print them out as you
# compute them.

def maxSlidingWindow(nums, k):
        result = []
        q = []
        
        for i in range(k):
                while q and nums[i] >= nums[q[-1]]:
                        q.pop()
                
                q.append(i)
        
        for i in range(k , len(nums)):
                result.append(nums[q[0]])
                while q and q[0] <= i - k:
                        q.pop(0)
                
                while q and nums[q[-1]] <= nums[i]:
                        q.pop()
                
                q.append(i)
        
        result.append(nums[q[0]])
        return result

print(maxSlidingWindow([10, 5, 2, 7, 8, 7], 3))
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
print(maxSlidingWindow([1,-1], 1))
print(maxSlidingWindow([1,3,1,2,0,5],3))
                