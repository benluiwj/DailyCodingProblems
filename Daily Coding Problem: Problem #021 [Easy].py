# Good morning! Here's your coding interview problem for today.

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly
# overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
def count_rooms(timings):
        starts = sorted(start for start, end in timings)
        ends = sorted(end for start, end in timings)
        
        n = len(timings)
        i, j = 0, 0
        current_overlaps = 0
        max_overlaps = 0
        
        while i < n and j < n:
                if starts[i] < ends[j]:
                        current_overlaps += 1
                        max_overlaps = max(max_overlaps, current_overlaps)
                        i += 1
                
                else:
                        current_overlaps -= 1
                        j += 1
        
        return max_overlaps        


assert count_rooms([(30, 75), (0, 50), (60, 150)]) == 2
assert count_rooms([[0, 30],[5, 10],[15, 20]]) == 2
assert count_rooms([[7,10],[2,4]]) == 1