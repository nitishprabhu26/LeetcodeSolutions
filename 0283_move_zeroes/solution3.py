# Approach #2 (Space Optimal, Operation Sub-Optimal) [Accepted]


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        # If the current element is not 0, then we need to append it just in front of last non 0 element we 
        # found. 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1

        # fill remaining array with 0's.
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
        return nums


nums = [0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))


# Complexity Analysis:
# Time Complexity: O(n). However, the total number of operations are still sub-optimal. The total operations 
# (array writes) that code does is n (Total number of elements).
# Space Complexity : O(1). Only constant space is used.
