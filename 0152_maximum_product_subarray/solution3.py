# Approach: Neetcode
# https://youtu.be/lXVy6YWFcRM

import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # optional
        if math.prod(nums) > 0:
            return math.prod(nums)

        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:
            temp = curMax * n

            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            res = max(curMax, res)

        return res   


nums = [3,4,5,1,2]
obj = Solution()
print(obj.maxProduct(nums))


# Complexity Analysis
# Time complexity : O(N) where N is the size of nums. The algorithm achieves linear runtime since we are going 
# through nums only once.
# Space complexity : O(1).