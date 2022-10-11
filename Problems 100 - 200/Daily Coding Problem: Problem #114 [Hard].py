# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given
# "hello/world:here", return "here/world:hello"

# Follow-up: Does your solution work for the following cases: "hello/world:here/",
# "hello//world:here"
def reverse_words(string, delimiters):
        words = []
        word = ''
        delimiter = ''
        delimiter_indexes = set()
        for i, char in enumerate(string):
                if char not in delimiters:
                        if delimiter:
                                words.append(delimiter)
                                delimiter_indexes.add(len(words)-1)
                                delimiter = ''
                        word += char
                
                else:
                        if word:
                                words.append(word)
                                word = ''
                        delimiter += char
        
        if word:
                words.append(word)
        
        if delimiter:
                words.append(delimiter)
                delimiter_indexes.add(len(words) - 1)
        
        print(words)
        print(delimiter_indexes)
        start = 0
        end = len(words) - 1
        while start <= end:
                while start in delimiter_indexes:
                        start += 1
                while end in delimiter_indexes:
                        end -= 1
                
                words[start], words[end] = words[end], words[start]
                start += 1
                end -= 1
        
        return ''.join(words)
                
                
                

print(reverse_words("hello//world:here", {"/", ":"}))
                