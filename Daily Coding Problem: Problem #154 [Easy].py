# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Implement a stack API using only a heap. A stack implements the following
# methods:

#  * push(item), which adds an element to the stack
#  * pop(), which removes and returns the most recently added element (or throws
#    an error if there is nothing on the stack)

# Recall that a heap has the following operations:

#  * push(item), which adds a new key to the heap
#  * pop(), which removes and returns the max value of the heap

import heapq

"""
stack is FIFO
use max heap to implement stack

have a counter whenever sth is pushed onto it. counter would be the time it would be pushed.


"""


class Stack:
        def __init__(self):
                # python heaps are min heaps but for the sake of qns gonna make it max by multiplying sth by -1
                self.heap = []
                self.timer = -1
        
        def push(self, item):
                heapq.heappush(self.heap, (self.timer, item))
                self.timer -= 1
        
        def pop(self):
                _, num = heapq.heappop(self.heap)
                return num

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
res = stack.pop()
print(res) 