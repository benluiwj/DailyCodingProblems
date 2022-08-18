# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Implement an LRU (Least Recently Used) cache. It should be able to be
# initialized with a cache size n, and contain the following methods:

#  * set(key, value): sets key to value. If there are already n items in the cache
#    and we are adding a new item, then it should also remove the least recently
#    used item.
#  * get(key): gets the value at key. If no such key exists, return null.

# Each operation should run in O(1) time.

from typing import *

"""

when there are n items, pop operation is O(1). deletion is O(n) since shift everything forward. append to back is O(1)

use a doubly-linked list. create a dictionary that maps the value to the node itself, then deletion would be O(1).


"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = value
            
            while len(self.cache) > self.capacity:
                self.cache.popitem(False)
            
            
        else:
            self.cache.pop(key)
            self.cache[key] = value

cache1 = LRUCache(1)
cache1.put(2,1)
cache1.get(2)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3,3)
assert cache.get(2) == None
cache.put(4, 4);

assert cache.get(1) == None;    
assert cache.get(3) == 3;    
assert cache.get(4) == 4 ;
        
        
        
        