# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Write a map implementation with a get function that lets you retrieve the value
# of a key at a particular time.

# It should contain the following methods:

#  * set(key, value, time): sets key to value for t = time.
#  * get(key, time): gets the key at t = time.

# The map should work like this. If we set a key at a particular time, it will
# maintain that value forever or until it gets set at a later time. In other
# words, when we get a key at a time, it should return the value that was set for
# that key set at the most recent time.

# Consider the following examples:

# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2


# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1


# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2

from collections import defaultdict

"""

notice that timings added are always increasing, this means that its actually sorted. to perform get, use binary search and get the closest to it. 

can actually just append values to a list.

"""

class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
                self.map[key][timestamp] = value
        
        else:
                self.map[key] = defaultdict()
                self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
                if timestamp in self.map[key]:
                        return self.map[key][timestamp]
                
                else:
                        prev_val = ""
                        prev_time = None
                        for k, val in self.map[key].items():
                                if k < timestamp:
                                        prev_val = val
                                        prev_time = k
                                
                                else:
                                        self.map[key][timestamp] = prev_val
                                        return prev_val
                                
                        self.map[key][timestamp] = prev_val
                        return prev_val
        
        return None

tm = TimeMap()
tm.set("love","high",10)
tm.set("love","low",20)
tm.get("love",25)

