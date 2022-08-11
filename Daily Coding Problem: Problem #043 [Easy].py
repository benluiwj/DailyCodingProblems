# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

#  * push(val), which pushes an element onto the stack
#  * pop(), which pops off and returns the topmost element of the stack. If there
#    are no elements in the stack, then it should throw an error or return null.
#  * max(), which returns the maximum value in the stack currently. If there are
#    no elements in the stack, then it should throw an error or return null.

# Each method should run in constant time.
"""

maintain the biggest element so far at every stack push

"""

class stack:
        def __init__(self):
                self.stack = []
                
        
        def push(self, val):
                biggest, _ = self.stack[-1]
                
                if val > biggest:
                        self.stack.append((val, val))
                
                else:
                        self.stack.append((biggest, val))
        
        def pop(self):
                if not stack:
                        return None
                
                _ , val = self.stack.pop()
                
                return val
        
        def max(self):
                if not stack:
                        return None
                
                return self.stack[-1][0]