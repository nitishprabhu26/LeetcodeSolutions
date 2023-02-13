# Approach 1: Prefix Sums with Linear Search
# https://leetcode.com/problems/random-pick-with-weight/solution/
# OR
# https://youtu.be/_z7UfMpYTXI

# Algorithm:
# First of all, before picking an index, we should first set up the playground, by generating a list of prefix 
# sums from a given list of numbers. The best place to do so would be in the constructor of the class, so that we 
# don't have to generate it again and again at the invocation of pickIndex() function.
# - In the constructor, we should also keep the total sum of the input numbers, so that later we could use this 
#   total sum to scale up the random number.
# For the pickIndex() function, here are the steps that we should perform.
# - Firstly, we generate a random number between 0 and 1. We then scale up this number, which will serve as our 
#   target offset.
# - We then scan through the prefix sums that we generated before by linear search, to find the first prefix sum 
#   that is larger than our target offset.
# - And the index of this prefix sum would be exactly the right place that the target should fall into. We return 
#   the index as the result of pickIndex() function.


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
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
            # OR 
            # if target <= prefix_sum:
                return i
            
# OR

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target <= prefix_sum:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Complexity Analysis:
# Let N be the length of the input list.
# Time Complexity:
# For the constructor function, the time complexity would be O(N), which is due to the construction of the prefix 
# sums.
# For the pickIndex() function, its time complexity would be O(N) as well, since we did a linear search on the 
# prefix sums.
# Space Complexity:
# For the constructor function, the space complexity would be O(N), which is again due to the construction of the 
# prefix sums.
# For the pickIndex() function, its space complexity would be O(1), since it uses constant memory. Note, here we 
# consider the prefix sums that it operates on, as the input of the function.