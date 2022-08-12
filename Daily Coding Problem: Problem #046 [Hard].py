# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a string, find the longest palindromic contiguous substring. If there are
# more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
# longest palindromic substring of "bananas" is "anana".

"""

take every contiguous substring and see if they are palindromes -> O(n^2) for every substring * O(n) for palindrome checking

notice that if a substring is not a palindrome, adding to both ends wont make it one. have to add to either end.
we can do bottom up dp in this case

dp[i][j] would be a boolean value, indicating whether s[i:j] is a palindrome

to check if s[i:j] is a palindrome, check if s[i+1:j-1] is a palindrome or not, provided s[i] == s[j]

if s[i] != s[j], see if can form palindrome by taking checking if s[i] == s[j-1] or s[i+1] == s[j], then proceed with the normal palindrome checking.

"""

from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[True for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        start = 0
        end = 0
        
        for i in range(n - 2, -1 , -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                
                else:
                    dp[i][j] = False
                
                if dp[i][j] and j - i + 1 > end - start + 1:
                    start = i
                    end = j
                

        
        return s[start:end+1]
        
sol = Solution()
print(sol.longestPalindrome("aabcdcb"))
print(sol.longestPalindrome("bananas"))
print(sol.longestPalindrome("cbbd"))