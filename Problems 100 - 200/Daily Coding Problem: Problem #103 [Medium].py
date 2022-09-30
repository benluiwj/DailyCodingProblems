# Good morning! Here's your coding interview problem for today.

# This problem was asked by Square.

# Given a string and a set of characters, return the shortest substring containing
# all the characters in the set.

# For example, given the string "figehaeci" and the set of characters {a, e, i},
# you should return "aeci".

# If there is no substring containing all the characters in the set, return null.
def shortest_substring(s, t):
        if len(s) < len(t):
            return ""

        table = dict()
        for char in t:
            if char in table:
                table[char] += 1
            
            else:
                table[char] = 1
        
        start = 0
        end = 0
        total_count = len(t)

        result = s + "a"
        n = len(s)

        while end < n:
            if s[end] in table:
                table[s[end]] -= 1
                if table[s[end]] >= 0:
                    total_count -= 1
            
            while not total_count:
                if s[start] in table:
                    if table[s[start]] == 0:
                        curr_length = end - start + 1
                        if curr_length < len(result):
                            result = s[start:end+1]
                        
                        total_count += 1
                    
                    table[s[start]] += 1
                
                start += 1
            
            end += 1
        
        if result == s + "a":
            return ""
        
        return result

print(shortest_substring("figehaeci", {"a", "e", "i"}))                     