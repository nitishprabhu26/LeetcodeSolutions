# Simple concatenation

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# OR
# Multiply by 2

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


nums = [1,2,1]
obj = Solution()
print(obj.getConcatenation(nums))
