# Approach 2: Dynamic Programming, Kadane's Algorithm
# OR
# Neetcode: https://youtu.be/5WZl3MMT0Eg

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += nums
            maxSub = max(maxSub, curSum)
        
        return maxSub


nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))


# Complexity Analysis:
# Time complexity: O(N), where N is the length of nums.
# We iterate through every element of nums exactly once.
# Space complexity: O(1)
# No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.