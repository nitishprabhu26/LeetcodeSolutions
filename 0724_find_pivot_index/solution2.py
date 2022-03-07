# Approach #1: Prefix Sum [Accepted]

# Intuition and Algorithm
# Let's say we knew S as the sum of the numbers, and we are at index i. If we knew the sum of numbers 'leftsum' 
# that are to the left of index i, then the other sum to the right of the index would just be 
# S - nums[i] - leftsum.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

# OR

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

        
nums = [1,7,3,6,5,6]
obj = Solution()
print(obj.pivotIndex(nums))


# Complexity Analysis:
# Time complexity : O(N), where N is the length of nums.
# Space complexity : O(1), the space used by leftsum and S.
