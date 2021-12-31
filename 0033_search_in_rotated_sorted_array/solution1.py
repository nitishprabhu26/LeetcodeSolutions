# Bruteforce approach

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1

nums = [4,5,6,7,0,1,2] 
target = 0
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Time complexity : O(n). 
# Space complexity : O(1).

