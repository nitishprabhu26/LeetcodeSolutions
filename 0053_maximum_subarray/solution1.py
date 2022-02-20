# Brute force approach [Time Limit Exceeded]

import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = -math.inf
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                iterative_subarray_sum = sum(nums[i:j+1])
                if iterative_subarray_sum > max_subarray_sum:
                    max_subarray_sum = iterative_subarray_sum
        return max_subarray_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))


# Complexity Analysis:
# Time complexity: O(N^3), where N is the length of nums.
# To actually generate all subarrays would take O(N^3) time.
# We use 2 nested for loops, with each loop iterating through nums. and a sum method which has a O(N) complexity.
# Space complexity: O(1)
# No matter how big the input is, we are only ever using 2 variables.