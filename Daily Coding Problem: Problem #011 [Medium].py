# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a
# prefix.

# For example, given the query string de and the set of strings [dog, deer, deal],
# return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to
# speed up queries.
class Node:
        def __init__(self, val="", isLast = False):
                self.val = val
                self.neighbors = dict()
                self.isLast = isLast 
        
        def get_query(self, query):
                curr = self
                for char in query:
                        if char in curr.neighbors:
                                curr = curr.neighbors[char]
                        else:
                                return []
                
                def helper(current, s):
                        if current.isLast:
                                return [s]
                        
                        res = []
                        for neighbor in current.neighbors:
                                dup = s + neighbor
                                res.extend(helper(current.neighbors[neighbor], dup))
                        
                        return res
                
                return helper(curr, query)

def autocomplete(query, strings):
        trie = Node()
        for string in strings:
                current = trie 
                for char in string:
                        if char not in current.neighbors:
                                current.neighbors[char] = Node(val = char)
                        
                        current = current.neighbors[char]
                
                current.isLast = True
        
        return trie.get_query(query)

print(autocomplete("dea", ["dog", "deer", "deal"]))
                        
                        