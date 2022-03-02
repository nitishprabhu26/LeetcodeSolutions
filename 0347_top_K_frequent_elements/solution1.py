# Approach 1: Heap
# Using heapq and nlargestt function
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

# Heap approach with O(Nlogk) time complexity. To ensure that O(Nlogk) is always less than O(NlogN), the 
# particular case k = N could be considered separately and solved in O(N) time.

# Algorithm:
# - The first step is to build a hash map: element -> its frequency. In Java, we use the data structure HashMap. 
# Python provides dictionary subclass Counter to initialize the hash map we need directly from the input array.
# This step takes O(N) time where N is a number of elements in the list.
# - The second step is to build a heap of size k using N elements. To add the first k elements takes a linear 
# time O(k) in the average case, and O(log1+log2+...+logk) = O(klogk) in the worst case. It's equivalent to 
# heapify implementation in Python. After the first k elements we start to push and pop at each step, N - k steps 
# in total. The time complexity of heap push/pop is O(logk) and we do it N - k times that means O((N−k)logk) time 
# complexity. Adding both parts up, we get O(Nlogk) time complexity for the second step.
# - The third and the last step is to convert the heap into an output array. That could be done in O(klogk) time.

# In Python, library heapq provides a method nlargest, which combines the last two steps under the hood and has 
# the same O(Nlogk) time complexity.

from typing import List
from collections import Counter
import heapq


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
        # OR
        return heapq.nlargest(k, count, key=count.get) 


nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))


# Complexity analysis:
# Time complexity : O(N logk) if k < N and O(N) in the particular case of N = k. That ensures time complexity to 
# be better than O(N logN).
# Space complexity : O(N + k) to store the hash map with not more N elements and a heap with k elements.

