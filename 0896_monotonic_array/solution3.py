# Approach 3: One Pass (Simple Variant)

# Intuition and Algorithm:
# To perform this check in one pass, we want to remember if it is monotone increasing or monotone decreasing.
# It's monotone increasing if there aren't some adjacent values A[i], A[i+1] with A[i] > A[i+1], and similarly for 
# monotone decreasing.
# If it is either monotone increasing or monotone decreasing, then A is monotonic.


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                increasing = False
            if nums[i] < nums[i+1]:
                decreasing = False

        return increasing or decreasing
            

nums = [1,2,2,3]
nums = [6,5,4,4]
obj = Solution()
print(obj.isMonotonic(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(1)