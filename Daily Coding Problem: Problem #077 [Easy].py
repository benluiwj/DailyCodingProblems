# Good morning! Here's your coding interview problem for today.

# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals
# where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1,
# 3), (4, 10), (20, 25)].

from typing import *

def is_overlap(interval1, interval2):
        start1, end1 = interval1
        start2, _ = interval2
        
        return start1 <= start2 <= end1

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0])
        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
                if is_overlap(merged_intervals[-1], intervals[i]):
                        merged_intervals[-1][0] = min(merged_intervals[-1][0], intervals[i][0])
                        merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
                
                else:
                        merged_intervals.append(intervals[i])
        
        return merged_intervals