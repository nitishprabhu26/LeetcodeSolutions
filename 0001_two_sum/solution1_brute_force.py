from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i, j


nums = [2, 6, 11, 15]
target = 8
obj = Solution()
print(obj.twoSum(nums, target))

# Complexity Analysis:
# Time complexity : O(n^2)
# Space complexity : O(1)
