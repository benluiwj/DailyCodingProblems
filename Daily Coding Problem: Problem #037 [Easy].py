# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1,
# 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.

def generate_power_set(nums):
        result = [[]]
        
        def helper(nums, index, current):                
                for i in range(index, len(nums)):
                        current.append(nums[i])
                        result.append(current.copy())
                        helper(nums, i + 1, current)
                        current.pop()
                
                
                
        
        helper(nums, 0, [])
        print(result)
        return result
        

generate_power_set([1,2,3])