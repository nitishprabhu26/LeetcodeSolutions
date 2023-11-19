# Approach: Using heapq.nlargest


import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = heapq.nlargest(self.k, nums)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]
        

# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))