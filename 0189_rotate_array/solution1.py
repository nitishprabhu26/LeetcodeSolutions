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
        # cant be the below code: since it errors out for the case nums = [1], k = 0
        # nums[:k], nums[k:] = nums[-k:] , nums[:-k]


nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
obj.rotate(nums, k)
print(nums)