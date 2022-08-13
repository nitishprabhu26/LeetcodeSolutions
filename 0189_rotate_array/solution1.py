# Array Slicing
# in place, No extra space used


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:k], nums[k:] = nums[-k:] , nums[:n-k]


nums = [1,2,3,4,5,6,7]
k = 6
obj = Solution()
obj.rotate(nums, k)
print(nums)