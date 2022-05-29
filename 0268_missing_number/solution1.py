# Linear search (Brute force approach)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums) + 1):
            if num not in nums:
                return num
        

nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))
