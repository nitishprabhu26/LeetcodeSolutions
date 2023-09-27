# Approach #3 Bit Manipulation [Accepted]
# OR
# Neetcode:
# https://youtu.be/WnPLSRLSANE

# Algorithm:
# Because we know that nums contains n numbers and that it is missing exactly one number on the range [0..n-1], 
# we know that n definitely replaces the missing number in nums. Therefore, if we initialize an integer to n 
# and XOR it with every index and value, we will be left with the missing number.
# eg: nums = [0, 1, 3, 4]
# missing   = 4 ∧ (0∧0) ∧ (1∧1) ∧ (2∧3) ∧ (3∧4)
#           = (4∧4) ∧ (0∧0) ∧ (1∧1) ∧ (3∧3) ∧ 2
#           = 0 ∧ 0 ∧ 0 ∧ 0 ∧ 2
#           = 2
 

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

# OR
# https://youtu.be/406y4hq66UM


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorArr = 0
        for i in nums:
            xorArr ^= i
        xorAll = 0
        for i in range(len(nums) + 1):
            xorAll ^= i
        return xorArr ^ xorAll



nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))


# Complexity Analysis
# Time complexity : O(n). 
# Assuming that XOR is a constant-time operation, this algorithm does constant work on n iterations, so the
# runtime is overall linear.
# Space complexity : O(1).
# This algorithm allocates only constant additional space.