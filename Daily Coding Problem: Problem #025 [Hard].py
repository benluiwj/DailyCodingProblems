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



"""

class Solution:
        def isMatch(self, s: str, p: str) -> bool:
                for i in range(len(p)):
                        if p[i] == ".":
                                continue
                        
                        elif p[i] == "*":
                                prev = p[i-1]
                                s_pter = i
                                diff = len(p) - (i + 1)
                                while s_pter != diff:
                                        if prev != "." and prev != s[s_pter]:
                                                return False
                                        
                                        s_pter += 1
                        
                        elif p[i] != s[i]:
                                return False
                
                return True
                                        
                                        
                                        
                                        


sol = Solution()

sol.isMatch("ab", ".*")