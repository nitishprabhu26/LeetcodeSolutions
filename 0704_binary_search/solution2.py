# Approach 2: Binary Search (Recursive Approach)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bsearch(nums, target, 0, len(nums)-1)

    def bsearch(self, nums, target, low, high):
        if high < low:
            return -1

        mid = low + (high-low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.bsearch(nums, target, low, mid-1)

        return self.bsearch(nums, target, mid+1, high)



nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Time complexity: O(logN).
# Space complexity : O(1) as it is a tail recursion.
