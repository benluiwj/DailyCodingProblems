# Good morning! Here's your coding interview problem for today.

# This problem was asked by Quora.

# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than one
# palindrome of minimum length that can be made, return the lexicographically
# earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can
# add three letters to it (which is the smallest amount to make a palindrome).
# There are seven other palindromes that can be made from "race" by adding three
# letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

from typing import *

"""

if start and end are the same letters, count min insertions for the rest of the word excluding start and end.
if start and end are different, add start and move one inwards. add end and move one inwards.

compare lengths first, then if the lengths are the same, take the shorter one.

initialise a table with n + 1 to allow for empty string.

"""

class Solution:
        def minInsertions(self, s: str) -> int:
                # if len(s) <= 1:
                #         return s
                
                # if s[0] == s[-1]:
                #         return s[0] + self.minInsertions(s[1:-1]) + s[-1]
                
                # return min(s[0] + self.minInsertions(s[1:]) + s[0], s[-1] + self.minInsertions(s[:-1]) + s[-1])
                if len(s) <= 1:
                        return s
                
                table = [['' for i in range(len(s) + 1)] for j in range(len(s) + 1)]
                
                for i in range(len(s)):
                        table[i][1] = s[i]
                
                for j in range(2, len(s) + 1):
                        for i in range(len(s) - j + 1):
                                first, last = s[i], s[j-1]
                                if first == last:
                                        table[i][j] = first + table[i + 1][j - 2] + last
                                else:
                                        one = first + table[i + 1][j - 1] + first
                                        two = last + table[i][j - 1] + last
                                        if len(one) < len(two):
                                                table[i][j] = one
                                        
                                        elif len(one) > len(two):
                                                table[i][j] = two
                                        
                                        else:
                                                table[i][j] = min(one, two)
                
                return table[0][-1]
                
                       
                
                
        
sol = Solution()

print(sol.minInsertions("zzazz"))