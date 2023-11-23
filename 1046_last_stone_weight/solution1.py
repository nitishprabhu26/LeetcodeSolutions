# Approach: Using Arrays and Sort
# OR
# Approach 1: Array-Based Simulation
# https://leetcode.com/problems/last-stone-weight/editorial/


from typing import List

# Simply sort inside the loop every time. Time complexity of O(N^2 log⁡ N).
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            firstMax = stones.pop()
            secondMax = stones.pop()
            if firstMax != secondMax:
                stones.append(firstMax - secondMax)
        return stones[0] if stones else 0
        

# OR
# Approach 1: Array-Based Simulation
# O(N^2).
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Swap the stone to be removed with the end.
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0


stones = [2,7,4,1,8,1]
# stones = [2,2]
obj = Solution()
print(obj.lastStoneWeight(stones))


# Complexity Analysis:
# Let N be the length of stones.
# Time complexity : O(N^2). The only non-O(1) method of StoneArray is index(). This method does a single pass 
# over the array, to find the index of the maximum value. This pass has a cost of O(N).
# Space complexity : O(1). We are not allocating any new space for data structures.