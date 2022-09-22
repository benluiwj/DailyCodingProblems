# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# Given an arithmetic expression in Reverse Polish Notation
# [https://en.wikipedia.org/wiki/Reverse_Polish_notation], write a program to
# evaluate it.

# The expression is given as a list of numbers and operands. For example: [5, 3,
# '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should
# return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) =
# 5.

# You can assume the given expression is always valid.
import math
from typing import *

"""
when we hit an operator, pop the last 2 elements and evaluate them
once done push it back into stack

"""

ADD = '+'
SUB = '-'
DIV = '/'
MUL = '*'

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == ADD:
                val1 = stack.pop()
                val2 = stack.pop()
                result = val2 + val1
                stack.append(result)
            
            elif token == SUB:
                val1 = stack.pop()
                val2 = stack.pop()
                result = val2 - val1
                stack.append(result)
            
            elif token == DIV:
                val1 = stack.pop()
                val2 = stack.pop()
                result = val2 / val1
                
                if result < 0:
                    result = math.ceil(result)
                
                else:
                    result = math.floor(result)
                
                stack.append(result)
            
            elif token == MUL:
                val1 = stack.pop()
                val2 = stack.pop()
                result = val2 * val1
                stack.append(result)
            
            else:
                stack.append(int(token))
        
        return stack[0]