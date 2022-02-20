# Approach 1: Brute Force [Time Limit Exceeded]

from math import prod
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result
        
# OR

# O(N^3) sice we use prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                calc_prod = prod(nums[i : j + 1])
                if calc_prod > result:
                    result = calc_prod
        return result


        
nums = [3,4,5,1,2]
obj = Solution()
print(obj.maxProduct(nums))

# Complexity Analysis:
# Time Complexity : O(N^2) where N is the size of nums. Since we are checking every possible contiguous subarray 
# following every element in nums we have quadratic runtime.
# Space Complexity : O(1) since we are not consuming additional space other than two variables: result to hold 
# the final result and accu to accumulate product of preceding contiguous subarrays.