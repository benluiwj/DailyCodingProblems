# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:

#  * record(order_id): adds the order_id to the log
#  * get_last(i): gets the ith last element from the log. i is guaranteed to be
#    smaller than or equal to N.

# You should be as efficient with time and space as possible.
class Log:
        def __init__(self, n):
                self.log = []
                self.length = n
                self.start = 0
        
        def record(self, order_id):
                if len(self.log) == self.start + self.length:
                        self.start += 1
                
                self.log.append(order_id)
        
        def get_last(self, i):
                return self.log[(self.start + i-1)]

log = Log(2)
log.record(1)
log.record(2)
log.record(3)

# [1 , 2 , 3]
#      ^

print(log.get_last(1)) # return 2
print(log.get_last(2)) # return 3