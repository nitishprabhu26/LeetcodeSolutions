# Approach 4: Use built-in tools.
# Python provides bisect module which supports binary search functions.

# Algorithm
# -   Use built-in tools to locate the rightmost insertion position idx.
# -   If idx > 0 and nums[idx - 1] = target, return true. Otherwise, return false.

# Note: bisect.bisect_right looks for the rightmost insertion position.
# Similar to-> Approach 2: Find Upper bound


import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the insertion position `idx`.
        idx = bisect.bisect_right(nums, target)

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1


# OR
# Similar to-> Approach 3: Find Lower bound

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the insertion position `idx`.
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1


nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Let N be the size of the input array nums.
# Time complexity: O(log N). The time complexity of the built-in binary search is O(log N).
# Space complexity : O(1). The built-in binary search only takes O(1) space.
