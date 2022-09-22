# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.

from time import sleep


def job_scheduler(f, n):
        sleep(n/1000)
        return f