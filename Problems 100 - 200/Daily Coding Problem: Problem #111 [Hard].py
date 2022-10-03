# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a word W and a string S, find all starting indices in S which are anagrams
# of W.

# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

"""

check every window to see if they are anagrams or not. to check whether a string is an anagram, determine whether all the of that window is 0

this runs in O(ws), where w is length of W and S is length S. 

to speed this up, have a total count

if the count at each is greater than 0, then we modify the total, otherwise we dont. 

in this regard, only when the value increases above 0, then we add to total. if the value decrease to 0 then we subtract from total. 

"""



from typing import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexes = []
        start = 0
        end = len(p) - 1
        
        anagrams = dict()
        for char in p:
            if char in anagrams:
                anagrams[char] += 1
            else:
                anagrams[char] = 1
                
        total = len(p)
        
        for i in range(end + 1):
            if s[i] in anagrams:
                anagrams[s[i]] -= 1
                if anagrams[s[i]] >= 0:
                    total -= 1
        
        while end < len(s) - 1:
            if total == 0:
                indexes.append(start)
            
            if s[start] in anagrams:
                anagrams[s[start]] += 1
                if anagrams[s[start]] > 0:
                    total += 1
            
            start += 1
            end += 1
            
            if s[end] in anagrams:
                anagrams[s[end]] -= 1
                if anagrams[s[end]] >= 0 :
                    total -= 1
        
        if total == 0:
            indexes.append(end)
        
        return indexes
                        
            
        

sol = Solution()

sol.findAnagrams("abab", "ab")