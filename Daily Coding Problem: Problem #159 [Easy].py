# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string, return the first recurring character in it, or null if there is
# no recurring character.

# For example, given the string "acbbac", return "b". Given the string "abcdef",
# return null.
"""

save the characters we have seen in a set
when a character is about to be added, see if its in the set already
if it is return it

"""
def first_recurring(s):
        table = set()
        
        for char in s:
                if char in table:
                        return char
                
                table.add(char)
        
        return None
                