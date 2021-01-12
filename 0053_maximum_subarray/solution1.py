class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_subarray_sum = 0
        for i in range(len(nums)):
            iterative_subarray_sum = 0
            for j in range(i+1, len(nums)):
                iterative_subarray_sum = sum(nums[i:j])
                if iterative_subarray_sum > max_subarray_sum:
                    max_subarray_sum = iterative_subarray_sum
        return max_subarray_sum


nums = [1]
# [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
obj.maxSubArray(nums)