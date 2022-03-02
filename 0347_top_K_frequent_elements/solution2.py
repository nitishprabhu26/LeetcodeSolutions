# Approach 1 : (similar)

# collections.Counter in Python has a most_common API
# most_common calls nlargest under the hood
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        return [x for x, y in Counter(nums).most_common(k)]


# Different approach : Youtube https://youtu.be/Vru4ooOMjX0

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        ans = []
        freq = {}
        
        # having a counter, element -> its frequency
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for key, val in freq.items():
            # just push the first k elements, later use heappushpop to push element and remove the lowest 
            # val(freq)
            if len(ans) < k:
                heapq.heappush(ans, [val, key])
            else:
                heapq.heappushpop(ans, [val, key])
        
        return [key for val, key in ans]


nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))


# Complexity analysis:
# Time complexity : O(N logk) if k < N and O(N) in the particular case of N = k. That ensures time complexity to 
# be better than O(N logN).
# Space complexity : O(N + k) to store the hash map with not more N elements and a heap with k elements.

