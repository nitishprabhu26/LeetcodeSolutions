# Approach 3: Circular Queue with Array

# Intuition:
# Other than the deque data structure, one could also apply another fun data structure called circular queue, 
# which is basically a queue with the circular shape.
# - The major advantage of circular queue is that by adding a new element to a full circular queue, it 
#   automatically discards the oldest element. Unlike deque, we do not need to explicitly remove the oldest element.
# - Another advantage of circular queue is that a single index suffices to keep track of both ends of the queue, 
#   unlike deque where we have to keep a pointer for each end.

# Algorithm:
# No need to resort to any library, one could easily implement a circular queue with a fixed-size array. The key 
# to the implementation is the correlation between the index of head and tail elements, which we could summarize 
# in the following formula:
# tail = (head + 1) mod size
# In other words, the tail element is right next to the head element. Once we move the head forward, we would 
# overwrite the previous tail element.


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# Complexity analysis:
# Time complexity : O(1), as we can see that there is no loop in the next(val) function.
# Space complexity : O(N), where N is the size of the circular queue.