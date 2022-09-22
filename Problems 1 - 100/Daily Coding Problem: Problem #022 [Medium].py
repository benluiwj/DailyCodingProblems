# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction, then
# return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
# "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath',
# 'and', 'beyond'].
def word_break(dictionary, string):
        # Time : O(2 ^ N)
        # def helper(dictionary, string, index):
        #         if index == len(string):
        #                 return [], True
                
        #         result = []
        #         current = ""
        #         for i in range(index, len(string)) :
        #                 current += string[i]
        #                 if current in dictionary:
        #                         result.append(current)
        #                         words, valid = helper(dictionary, string, i + 1)
        #                         if valid:
        #                                 result.extend(words)
        #                                 return result, True
                                
        #                         else:
        #                                 result.pop()
                        
                
        #         return result, False
        
        # res , valid = helper(dictionary, string, 0)
        # if valid:
        #         return res
        starts = {0: ""}
        
        for i in range(len(string) + 1):
                new_starts = starts.copy()
                for start_index, _ in starts.items():
                        word = string[start_index:i]
                        if word in dictionary:
                                new_starts[i] = word
                
                starts = new_starts.copy()
        
        result = []
        current_length = len(string)
        if current_length not in starts:
                return 
        
        while current_length > 0:
                word = starts[current_length]
                result.append(word)
                current_length -= len(word)
        
        return list(reversed(result))
                        
        
        
        
        


assert word_break({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond") == ['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond']
assert word_break({'quick', 'brown', 'the', 'fox'},"thequickbrownfox") == ['the', 'quick', 'brown', 'fox']
assert word_break({'the', 'theremin'}, 'theremin') == ['theremin']