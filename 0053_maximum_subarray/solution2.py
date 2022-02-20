# Approach 1: Optimized Brute Force [Time Limit Exceeded]

# Intuition:
# A little optimization, we can achieve brute force in O(N^2) time. The trick is to recognize that all of the 
# subarrays starting at a particular value will share a common prefix.

# Algorithm:
# 1. Initialize a variable maxSubarray = -infinity to keep track of the best subarray. We need to use negative 
# infinity, not 0, because it is possible that there are only negative numbers in the array.
# 2. Use a for loop that considers each index of the array as a starting point.
# 3. For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the 
# starting index, adding each element to currentSubarray. Every time we add an element it represents a possible 
# subarray - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.
# 4. Return maxSubarray.

import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))


# Complexity Analysis:
# Time complexity: O(N^1), where N is the length of nums.
# We use 2 nested for loops, with each loop iterating through nums.
# Space complexity: O(1)
# No matter how big the input is, we are only ever using 2 variables: ans and currentSubarray.