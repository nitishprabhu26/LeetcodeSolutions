# Approach : Using built in method for LCM
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/discuss/2808839/Python-use-Python's-LCM-(explained)


import math
from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        cnt = 0

        for i in range(0, len(nums)):       # [1] for every initial number, try extending
            l = nums[i]                     #     a continuous sequence of numbers
            for j in range(i, len(nums)):  
                l = math.lcm(l,nums[j])     # [2] once LCM becomes 'k', each subsequent number
                if l == k : cnt += 1        #     that don't increase this value will give one
                if l > k  : break           #     more valid subarray
            
        return cnt


nums = [3,6,2,7,1]
k = 6
obj = Solution()
print(obj.subarrayLCM(nums, k))


# Complexity Analysis:
# Time complexity : O(N * N).
# Space complexity : O(1).