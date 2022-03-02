# Approach 1: (Similar)
# https://youtu.be/Gj4-8sRi7W0

import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        c = Counter(nums) 
        
        # sort the dictionary, key is the no of times it appears
        # reverse it so that most freq elements are on top (descending order)
        c = sorted(c, key = lambda x : c[x], reverse = True)
        
        return c[:k]

# OR (using heap)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        c = Counter(nums) 
        
        # negative to make it max heap
        c = [(-v, k) for k, v in c.items()]
        heapq.heapify(c)
        output = []
        
        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])
        
        return output


nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))


# Complexity analysis:
# Time complexity : O(N logk) if k < N and O(N) in the particular case of N = k. That ensures time complexity to 
# be better than O(N logN).
# Space complexity : O(N + k) to store the hash map with not more N elements and a heap with k elements.

