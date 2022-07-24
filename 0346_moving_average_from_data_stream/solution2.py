# Approach 2: Double-ended Queue

# Intuition:
# We could do better than the first approach in both time and space complexity.
# 1. First of all, one might notice that we do not need to keep all values from the data stream, but rather the 
#    last n values which falls into the moving window.
#    -  By definition of the moving window, at each step, we add a new element to the window, and at the same time 
#       we remove the oldest element from the window. Here, we could apply a data structure called double-ended 
#       queue (a.k.a deque) to implement the moving window, which would have the constant time complexity (O(1)) 
#       to add or remove an element from both its ends. With the deque, we could reduce the space complexity down 
#       to O(N) where N is the size of the moving window.
# 2. Secondly, to calculate the sum, we do not need to reiterate the elements in the moving window.
#    -  We could keep the sum of the previous moving window, then in order to obtain the sum of the new moving 
#       window, we simply add the new element and deduce the oldest element. With this measure, we then can reduce 
#       the time complexity to constant.

# Algorithm:
# Definition of the deque from Python:
# Deques are a generalization of stacks and queues. Deques support thread-safe, memory efficient appends and pops 
# from either side of the deque with approximately the same O(1) performance in either direction.


from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# Complexity analysis:
# Time complexity : O(1), as we explained in intuition.
# Space complexity : O(N), where N is the size of the moving window.