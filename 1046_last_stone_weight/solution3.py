# Approach 3: Heap-Based Simulation
# https://leetcode.com/problems/last-stone-weight/editorial/
# OR
# Neetcode: https://youtu.be/B-QCq79-Vfw?si=sbcyVzcADRhhH3bX


# Intuition
# Approach 1 found and removed the maximum stones in O(N) time, and added the new stone in O(1) time. 
# Approach 2 inverted this, as finding and removing the maximum stones took O(1) time, but adding the new stone 
# took O(N) time. In both cases, we're left with an overall time complexity of O(N) per stone-smash turn.
# We want to find a solution that makes both removing the maximums, and adding a new stone, less than O(N).

# Algorithm:
# While most programming languages have a Heap/ Priority Queue data structure, some, such as Python and Java, 
# only have Min-Heap. Just as the name suggests, this is a Heap that instead of always returning the maximum 
# item, it returns the minimum. There are two solutions to this problem:
# 1. Multiply all numbers going into the heap by -1, and then multiply them by -1 to restore them when they 
#    come out.
# 2. Pass a comparator in (language-dependent).


import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0


stones = [2,7,4,1,8,1]
# stones = [2,2]
obj = Solution()
print(obj.lastStoneWeight(stones))


# Complexity Analysis:
# Let N be the length of stones.
# Time complexity : O(NlogN). 
# Converting an array into a Heap takes O(N) time (it isn't actually sorting; it's putting them into an order 
# that allows us to get the maximums, each in O(logN) time).
# Like before, the main loop iterates up to N−1 times. This time however, it's doing up to three O(log⁡ N)
# operations each time; two removes, and an optional add. Like always, the three is an ignored constant. This 
# means that we're doing N⋅O(log⁡ N) = O(NlogN) operations.
# Space complexity : O(1). In Python, converting a list to a heap is done in place, requiring O(1) auxiliary 
# space, giving a total space complexity of O(1).