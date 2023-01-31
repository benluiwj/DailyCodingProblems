# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string, split it into as few strings as possible such that each string
# is a palindrome.

# For example, given the input string racecarannakayak, return ["racecar", "anna",
# "kayak"].

# Given the input string abc, return ["a", "b", "c"].
from typing import * 

"""

fewest means longest palindromes.

naively take every substring and see if its palindrome.
palindrome checking done in O(n) time.
taking every substring done in O(n^2) time
total time would be O(n^3)

to express this recursively,
split the string into 3 different kinds, 
1) first 2 letters are the same, take the mid
2) take the front
3) take the back

possible to get palindromes of each index in a matrix then perform dfs




"""

class Solution:
    # need to optimise the dfs portion to prevent TLE
    def dfs(self, matrix, current_parts, index, result_parts):
        if index == len(matrix):
            if len(result_parts) > len(current_parts):
                result_parts = current_parts[::]
            
            return result_parts
        
        for i in range(index, len(matrix)):
            if matrix[index][i]:
                current_parts.append([index , i])
                result_parts = self.dfs(matrix, current_parts, i+1, result_parts)
                current_parts.pop()
        
        return result_parts
    
    
    def minPartitions(self, s: str) -> List[str]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                dp[i][j] = True
        
        for i in range(n - 2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
            
        result = []    
        for i in range(len(s)):
            result.append([i,i])
            
        for i in range(n):
            if dp[0][i]:
                result = self.dfs(dp,[[0,i]], i+1, result)
        
        result_part = []
        for start, end in result:
            result_part.append(s[start:end+1])
        
        return result_part
                

print(Solution().minPartitions("racecarannakayak"))