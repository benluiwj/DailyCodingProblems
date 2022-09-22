# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def well_balanced(brackets):
        stack = []
        open_brackets = {'(', '[', '{'}
        close_brackets = {')', ']', '}'}
        for bracket in brackets:
                if bracket in open_brackets:
                        stack.append(bracket)
                
                else:
                        if not stack:
                                return False
                        
                        if bracket == ')' and stack[-1] == '(':
                                stack.pop()
                        
                        elif bracket == ']' and stack[-1] == '[':
                                stack.pop()
                        
                        elif bracket == '}' and stack[-1] == '{':
                                stack.pop()
                        
                        else:
                                return False
        
        return len(stack) == 0