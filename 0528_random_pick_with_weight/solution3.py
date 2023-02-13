# Approach 2: Prefix Sums with Binary Search
# https://leetcode.com/problems/random-pick-with-weight/solution/

# Intuition
# We could improve the above approach by replacing the linear search with the binary search, which then can reduce 
# the time complexity of the pickIndex() function from O(N) to O(logN).
# As a reminder, the condition to apply binary search on a list is that the list should be sorted, either in 
# ascending or descending order. For the list of prefix sums that we search on, this condition is guaranteed.

# Algorithm:
# We could base our implementation largely on the previous approach. In fact, the only place we need to modify is 
# the pickIndex() function, where we replace the linear search with the binary search.


import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Complexity Analysis:
# Let N be the length of the input list.
# Time Complexity:
# For the constructor function, the time complexity would be O(N), which is due to the construction of the prefix 
# sums.
# For the pickIndex() function, this time its time complexity would be O(logN), since we did a binary search on 
# the prefix sums.
# Space Complexity:
# For the constructor function, the space complexity would be O(N), which is again due to the construction of the 
# prefix sums.
# For the pickIndex() function, its space complexity would be O(1), since it uses constant memory. Note, here we 
# consider the prefix sums that it operates on, as the input of the function.