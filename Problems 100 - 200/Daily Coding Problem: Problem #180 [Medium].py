# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a stack of N elements, interleave the first half of the stack with the
# second half reversed using only one other queue. This should be done in-place.

# Recall that you can only push or pop from a stack, and enqueue or dequeue from a
# queue.

# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

# Hint: Try working backwards from the end state.

"""

without constraints, take the second half, reverse it.
create a new array and add from the first half then second half

Solution intuition:
consider 1 2 3 4 5
pairing of queue of (5,4) and stack [3,2,1], pop from stack then take from queue
pairing can be obtained from a queue of (3,2,1,5,4), which is a rotation of the initial to the left by 2
 
"""

from typing import * 
from queue import Queue

def interleave(stack):
        q = Queue()
        
        for i in range(1, len(stack)):
                for _ in range(i, len(stack)):
                        val = stack.pop()
                        q.put(val)
                stack.append(q.get())
                while not q.empty():
                        stack.append(q.get())
        
        return stack
                
                
        
print(interleave([1,2,3,4,5]))
print(interleave([1,2,3,4]))        
