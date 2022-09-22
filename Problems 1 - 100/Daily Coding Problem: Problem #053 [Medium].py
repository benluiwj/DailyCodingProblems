# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in,
# first-out) data structure with the following methods: enqueue, which inserts an
# element into the queue, and dequeue, which removes it.
"""

one stack is for popping, the other for pushing

when elements are enqueued, they are pushed onto the the pushing stack

when elements are dequeued,

1) if the pop stack has elements, just pop from there
2) if the pop stack is empty, transfer everything from push stack into pop stack and pop the top

"""


from typing import *

class MyQueue:

    def __init__(self):
        self.popstack = []
        self.pushstack = []
        

    def push(self, x: int) -> None:
        self.pushstack.append(x)
        

    def pop(self) -> int:
        if self.popstack:
            return self.popstack.pop()
        
        while self.pushstack:
            val = self.pushstack.pop()
            self.popstack.append(val)
        
        return self.popstack.pop()

    def peek(self) -> int:
        if self.popstack:
            return self.popstack[-1]
        
        while self.pushstack:
            val = self.pushstack.pop()
            self.popstack.append(val)
        
        return self.popstack[-1]
        

    def empty(self) -> bool:
        return len(self.popstack) == 0 and len(self.pushstack) == 0
    
myQueue = MyQueue()

myQueue.push(1);
myQueue.push(2); 
assert myQueue.peek() == 1; 
assert myQueue.pop() == 1; 
assert myQueue.empty() == False; 