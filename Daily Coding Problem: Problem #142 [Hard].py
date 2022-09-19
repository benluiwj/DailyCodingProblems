# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You're given a string consisting solely of (, ), and *. * can represent either a 
# (, ), or an empty string. Determine whether the parentheses are balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.

"""

not possible to greedily close -> (*) = (() => falsen when should be balanced

when we reach * can just expand iterate through possible ones and try them recursively

if any returns true we continue otherwise we return false

dfs?


"""

STAR = ["(", ")", ""]

def validParenthesis(s):
        stack = []
        
        def helper(stack, index):
                for i in range(index + 1, len(s)):
                        char = s[i]
                        if char == '(':
                                stack.append(i)
                        elif char == ')':
                                if stack[-1] == '(':
                                        stack.pop()
                                else:
                                        stack.append(char)
                        
                        else:
                                for char in STAR:
                                        stack.append(char)
                                        result = helper(stack, i)
                                        if result:
                                                return result
                                        
                                        stack.pop()
                
                return len(stack) == 0
        
        return helper(stack, -1)


assert validParenthesis('(()*') == validParenthesis('(*)')