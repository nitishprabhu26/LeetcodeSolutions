# Approach 1 : (similar)

# collections.Counter in Python has a most_common API
# most_common calls nlargest under the hood

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        return [x for x, y in Counter(nums).most_common(k)]


# Complexity analysis:
# Time complexity : O(N logk).
# If we don't specify a number of returned elements(k), most_common returns a sorted list of the counts. This is 
# an O(n log n) algorithm (or O(n)? check below link). 
# Else if k is specified, its O(n log k) since it uses nlargest under the hood.
# https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
# Space complexity : O(N + k) to store the hash map with not more N elements and a heap with k elements.


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
            # push the first k elements, later use heappushpop to push element and remove the lowest val (freq)
            # When we push/pop list with 2 elements, heap considers the 1st value(list[0]) to order heap
            # also, if list[0] of any 2 or more elements are same, then it checks for list[1], and so on.
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
# Time complexity : O(N logk).
# Space complexity : O(N + k) to store the hash map with not more N elements and a heap with k elements.

