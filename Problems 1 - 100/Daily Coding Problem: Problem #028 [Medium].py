# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.

# More specifically, you should have as many words as possible in each line. There
# should be at least one space between each word. Pad extra spaces when necessary
# so that each line has exactly length k. Spaces should be distributed as equally
# as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side
# with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

"""

count number of spaces - by default 1 space is 1 letter
count the length of the words

if the length of the words + number of spaces exceed k when we add a new word,

get number of characters allocated to spaces
divide by number of spaces

if theres a remainder, increase from left.


"""
def add_words(k, text_length, words, space_count):
        chars_for_space = k - text_length
        
        if len(words) == 1:
                result = words[0] + " " * chars_for_space
                return result
        
        
        if space_count:
                size_of_space = chars_for_space // space_count
                remainder = chars_for_space % space_count
                        
        result = ""
                        
        for word in words:
                result += word
                if remainder:
                        result += " " * (size_of_space + 1)
                        remainder -= 1
                elif space_count:
                        result += " " * (size_of_space)
                                
                space_count -= 1
                        
        return result


def justify_text(words, k):
        result_sentence = []
        current = []
        space_count = 0
        text_length = 0
        
        for word in words:
                word_length = len(word)
                if text_length + space_count + 1 + word_length > k:
                        sentence = add_words(k, text_length, current, space_count)
                        
                        result_sentence.append(sentence)
                        
                        current = []
                        space_count = 0
                        text_length = 0
                
                current.append(word)
                text_length += word_length
                space_count = len(current) - 1
        
        if current:
                sentence = add_words(k , text_length, current, space_count)
                
                result_sentence.append(sentence)
        
        return result_sentence

# assert justify_text(["the", "quick", "brown", "fox", "jumps","over", "the", "lazy", "dog"], 16) == ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]

print(justify_text(["What","must","be","acknowledgment","shall","be"], 16))
print(justify_text(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))