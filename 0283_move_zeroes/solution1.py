# Using remove and append methods

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums

nums = [ 0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))

# Complexity Analysis
# Time Complexity: O(n^2). 
# remove - O(n), append - O(1) amortized. considering the for loop.
# Space Complexity : O(1).

