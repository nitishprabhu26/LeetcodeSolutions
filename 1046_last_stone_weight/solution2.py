# Approach 2: Sorted Array-Based Simulation
# https://leetcode.com/problems/last-stone-weight/editorial/

# Note: This approach is no better than Approach 1. We're only including so that we can look at why it doesn't 
# work as well as one might initially assume. See Approach 3 for the optimal approach.

# To simplify the search-for-maximum process, we could instead maintain a sorted array. We'd need to sort the 
# array at the start, and then ensure that each time we need to add a stone back, that we're maintaining the 
# sorted order.

# Unfortunately, inserting a stone into a sorted array is an O(N) operation. While we can use binary search to 
# determine where we should put it, inserting it still ultimately requires shifting all of the stones after it 
# down by one place. This makes the approach no better than the previous one from a complexity point-of-view 
# (in fact, it's actually worse because the space complexity is now unlikely to be O(1)).


import bisect
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0

# An alternative to this approach is to simply sort inside the loop every time. This will be even worse, with a 
# time complexity of O(N^2 log⁡ N).

stones = [2,7,4,1,8,1]
# stones = [2,2]
obj = Solution()
print(obj.lastStoneWeight(stones))


# Complexity Analysis:
# Let N be the length of stones.
# Time complexity : O(N^2). 
# The first part of the algorithm is sorting the list. This has a cost of O(N log⁡ N).
# Like before, we're repeating the main loop up to N−1 times. And again, we're doing an O(N) operation each 
# time; adding the new stone back into the array, maintaining sorted order by shuffling existing stones along 
# to make space for it.
# Space complexity : O(1). We are not allocating any new space for data structures.