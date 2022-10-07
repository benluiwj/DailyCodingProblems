# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a sorted list of integers, square the elements and give the output in
# sorted order.

# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
def squares_of_sorted(arr):
        result = []
        start = 0
        end = len(arr) -1
        while start <= end:
                if arr[start] ** 2 > arr[end] ** 2:
                        result.append(arr[start] ** 2)
                        start += 1
                elif arr[end] ** 2 > arr[start] ** 2:
                        result.append(arr[end] ** 2)
                        end -= 1
                else:
                        result.append(arr[start] ** 2)
                        result.append(arr[end] ** 2)
                        end -= 1
                        start += 1
        
        return result