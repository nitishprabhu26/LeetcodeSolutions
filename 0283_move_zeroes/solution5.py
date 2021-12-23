# Neetcode
# https://youtu.be/aayNRwUN3Do
# Having 2 pointers, one slow pointer (l) and other fast pointer (r)
# swapping on encountering a non zero element and also incrementing slow pointer

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums


nums = [0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))


# Complexity Analysis:
# Space Complexity : O(1). Only constant space is used.
# Time Complexity: O(n). However, the total number of operations are optimal. The total operations (array writes)
# that code does is Number of non-0 elements.
# This gives us a much better best-case (when most of the elements are 0) complexity than last solution. 
# However, the worst-case (when all elements are non-0) complexity for both the algorithms is same.
