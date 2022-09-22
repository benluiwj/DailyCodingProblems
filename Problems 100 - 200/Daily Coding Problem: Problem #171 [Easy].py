# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# You are given a list of data entries that represent entries and exits of groups
# of people into a building. An entry looks like this:

# {"timestamp": 1526579928, count: 3, "type": "enter"}

# This means 3 people entered the building. An exit looks like this:

# {"timestamp": 1526580382, count: 2, "type": "exit"}

# This means that 2 people exited the building. timestamp is in Unix time
# [https://en.wikipedia.org/wiki/Unix_time].

# Find the busiest period in the building, that is, the time with the most people
# in the building. Return it as a pair of (start, end) timestamps. You can assume
# the building always starts off and ends up empty, i.e. with 0 people inside.
from typing import * 

"""

sort by timestamp

supppose we have enter(2), enter(3), exit(4), enter(5), exit(6)

[2 5 1 6 0]
"""
EXIT = "exit"
ENTER = "enter"

def busiest_time(data):
        sorted_data = sorted(data, key = lambda x : x["timestamp"])
        cumulative_ppl = [0]
        timestamp_arr = [0]
        index = -1
        biggest = 0
        for i,data in enumerate(sorted_data):
                timestamp, count, type = data.values()
                timestamp_arr.append(timestamp)
                last = cumulative_ppl[-1]
                current_ppl = None
                if type == EXIT:
                        current_ppl = last - count
                else:
                        current_ppl = last + count
                
                if biggest < current_ppl:
                        biggest = current_ppl
                        index = i
                
                cumulative_ppl.append(current_ppl)
        
        
        
        return [timestamp_arr[index], timestamp_arr[index+1]] if index < len(data) else [timestamp_arr[index], timestamp_arr[index] + 1]