# Using append

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums


# OR
# Create new result array and then assign values

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (2 * len(nums))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans


nums = [1,2,1]
obj = Solution()
print(obj.getConcatenation(nums))
