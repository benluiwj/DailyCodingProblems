# Good morning! Here's your coding interview problem for today.

# This problem was asked Microsoft.

# Using a read7() method that returns 7 characters from a file, implement readN(n)
# which reads n characters.

# For example, given a file with the content “Hello world”, three read7() returns
# “Hello w”, “orld” and then “”.

def read7():
        pass

def readN(n):
        if n % 7 == 0:
                product = n // 7
                for _ in range(product):
                        read7()
                return
        
        product = n // 7
        for _ in range(product + 1):
                read7()
        