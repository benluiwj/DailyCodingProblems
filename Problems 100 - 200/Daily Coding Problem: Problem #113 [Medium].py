# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string of words delimited by spaces, reverse the words in string. For
# example, given "hello world here", return "here world hello"

# Follow-up: given a mutable string representation, can you perform this operation
# in-place?

def reverse(s):
        start = 0
        end = len(s)-1
        while start <= end:
                s[start] , s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        return s


class Solution:
    def reverseWords(self, s: str) -> str:
        s.trim()
        new_s = s.split()
        return reverse(s)
        