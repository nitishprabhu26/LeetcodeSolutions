# Approach 1: Array or List

# Intuition:
# We keep track of all the incoming values with the data structure of Array or List. Then from the data structure, 
# later we retrieve the necessary elements to calculate the average.

# Algorithm:
# 1. First, we initialize a variable queue to store the values from the data stream, and the variable n for the 
#    size of the moving window.
# 2. At each invocation of next(val), we first append the value to the queue. We then retrieve the last n values 
#    from the queue, in order to calculate the average.


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []
        
    def next(self, val: int) -> float:
        self.queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(self.queue[-self.size:])

        return window_sum / min(len(self.queue), self.size)
        

# OR
# (same as above, but using new array and variable)

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []
        
    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# Complexity analysis:
# Time complexity : O(N) where N is the size of the moving window, since we need to retrieve N elements from the 
# queue at each invocation of next(val) function.
# Space complexity : O(M), where M is the length of the queue which would grow at each invocation of the next(val) 
# function.

