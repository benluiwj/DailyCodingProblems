# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of
# numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle
# numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
# print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

from typing import *
from heapq import *

class MedianFinder:
        def __init__(self):
                self.min_heap = []
                self.max_heap = []
                
        
        def addNum(self, num: int) -> None:
                if not self.min_heap and not self.max_heap:
                        heappush(self.max_heap, -num)
                
                elif -1 * self.max_heap[0] < num:
                        heappush(self.min_heap, num)
                
                else:
                        heappush(self.max_heap, -num)
                
                # rebalance st diff in length <= 1
                
                while len(self.max_heap) < len(self.min_heap) or abs(len(self.max_heap) - len(self.min_heap)) > 1 :
                        if len(self.max_heap) > len(self.min_heap):
                                val = -1 * heappop(self.max_heap)
                                heappush(self.min_heap, val)
                        
                        else:
                                val = heappop(self.min_heap)
                                heappush(self.max_heap, -val)
                                
        
        def findMedian(self) -> float:
                max_length = len(self.max_heap)
                min_length = len(self.min_heap)
                is_odd = (max_length + min_length) % 2 == 1
                
                if is_odd:
                        if max_length > min_length:
                                return self.max_heap[0] * -1
                        
                        else:
                                return self.min_heap[0]
                
                else:
                        return (self.max_heap[0] * -1 + self.min_heap[0]) / 2 