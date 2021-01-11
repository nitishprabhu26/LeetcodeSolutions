class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length_array = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums

nums = [ 0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))