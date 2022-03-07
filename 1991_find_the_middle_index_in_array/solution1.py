# Approach : O(N^2) [Time Limit Exceeded] in 724 - but passes all Test cases here
# Here we calculate sum using sum method within the for loop

from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]): return i
        return -1


nums = [1,7,3,6,5,6]
obj = Solution()
print(obj.findMiddleIndex(nums))


# Complexity Analysis:
# Time complexity : O(N^2).
# Space complexity : O(1).
