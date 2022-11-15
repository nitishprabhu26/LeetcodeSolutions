# Approach : Using built in method for GCD


import math
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(0, len(nums)):       # [1] for every initial number, try extending
            l = nums[i]                     #     a continuous sequence of numbers
            for j in range(i, len(nums)):  
                l = math.gcd(l,nums[j])     # [2] once GCD becomes 'k', each subsequent number
                if l == k : cnt += 1        #     that don't decrease this value will give one
                if l < k  : break           #     more valid subarray
            
        return cnt


nums = [9,3,1,2,6,3]
k = 3
obj = Solution()
print(obj.subarrayGCD(nums, k))


# Complexity Analysis:
# Time complexity : O(N * N).
# Space complexity : O(1).