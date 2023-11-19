# Approach: Heap
# https://leetcode.com/problems/kth-largest-element-in-a-stream/editorial/
# OR
# Neetocde: https://youtu.be/hOjcdrqMoQ8?si=e0ciY_WANdyWSCvZ


import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

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


# Complexity Analysis:
# Given N as the length of nums and M as the number of calls to add(),
# Time complexity : O(N⋅log(N) + M⋅log(k)).
# The time complexity is split into two parts. First, the constructor needs to turn nums into a heap of size k. 
# In Python, heapq.heapify() can turn nums into a heap in O(N) time. Then, we need to remove from the heap 
# until there are only k elements in it, which means removing N - k elements. Since k can be, say 1, in terms 
# of big O this is N operations, with each operation costing log(N). Therefore, the constructor costs
# O(N + N⋅log⁡(N)) = O(N⋅log⁡(N)).
# Next, every call to add() involves adding an element to heap and potentially removing an element from heap. 
# Since our heap is of size k, every call to add() at worst costs O(2∗log⁡(k)) = O(log⁡(k)). That means M calls 
# to add() costs O(M⋅log⁡(k)).
# Space complexity : O(N). The only extra space we use is the heap. While during add() calls we limit the size 
# of the heap to k, in the constructor we start by converting nums into a heap, which means the heap will 
# initially be of size N.