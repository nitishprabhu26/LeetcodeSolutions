# Approach 2: Dynamic Programming, Kadane's Algorithm [Best approach]
# OR
# https://youtu.be/jnoVtCKECmQ

# Intuition:
# Any subarray whose sum is positive is worth keeping. Let's start with an empty array, and iterate through the 
# input, adding numbers to our array as we go along. Whenever the sum of the array is negative, we know the entire 
# array is not worth keeping, so we'll reset it back to an empty array.
# However, we don't actually need to build the subarray, we can just keep an integer variable current_subarray and 
# add the values of each element there. When it becomes negative, we reset it to 0 (an empty array).

# Algorithm:
# 1. Initialize 2 integer variables. Set both of them equal to the first value in the array.
#   -   currentSubarray will keep the running count of the current subarray we are focusing on.
#   -   maxSubarray will be our final return value. Continuously update it whenever we find a bigger subarray.
# 2. Iterate through the array, starting with the 2nd element (as we used the first element to initialize our 
#    variables). For each number, add it to the currentSubarray we are building. If currentSubarray becomes 
#    negative, we know it isn't worth keeping, so throw it away. Remember to update maxSubarray every time we 
#    find a new maximum.
# 3. Return maxSubarray.

# Implementation:
# A clever way to update currentSubarray is using currentSubarray = max(num, currentSubarray + num). If 
# currentSubarray is negative, then num > currentSubarray + num.

import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))


# Complexity Analysis:
# Time complexity: O(N), where N is the length of nums.
# We iterate through every element of nums exactly once.
# Space complexity: O(1)
# No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.