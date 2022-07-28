# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Implement regular expression matching with the following special characters:

#  * . (period) which matches any single character
#  * * (asterisk) which matches zero or more of the preceding element

# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string "raymond"
# should return false.

# Given the regular expression ".*at" and the string "chat", your function should
# return true. The same regular expression on the string "chats" should return
# false.

from typing import *

"""
if its a dot, just match normally, shift pointers forward

if its *, get previous and match as per noraml

how to stop in the case of something like:

chat, .*at

stop -> go till the end see if can
if cannot, continue and try again the next time the next element match


is_matched -> check whether text empty and whether the first letter of pattern is . or same as text

dp method:

initialise boolean array length of text



"""
class Solution(object):
        def isMatch(self, text, pattern):
                if not pattern:
                        return not text
                
                # first_match = bool(text) and pattern[0] in {text[0], '.'}
                
                # if len(pattern) >= 2 and pattern[1] == '*':
                #         return (self.isMatch(text, pattern[2:]) or
                #                 first_match and self.isMatch(text[1:], pattern))
                # else:
                #         return first_match and self.isMatch(text[1:], pattern[1:])
                
                t = len(text)
                p = len(pattern)
                dp = [[False for _ in range(t + 1)] for _ in range(p + 1)]
                
                # last element is the empty string, hence they are both equal
                dp[-1][-1] = True
                
                for i in range(t - 1, -1 , -1):
                        for j in range(p - 1, -1 , -1):
                                first_match = i < t and pattern[j] in {text[i], '.'}
                                
                                if j + 1 < p and p[j+1] == "*":
                                        dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                                
                                else:
                                        dp[i][j] = first_match and dp[i+1][j+1]
                
                return dp[0][0]
                
                
                        
                                        
                                        
                                        
                                        


sol = Solution()

sol.isMatch("ab", ".*")