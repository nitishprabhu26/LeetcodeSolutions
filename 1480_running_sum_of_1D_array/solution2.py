# Approach 1: Using Separate Space

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        listRunningSum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            listRunningSum.append(sum)
        return listRunningSum


# https://leetcode.com/problems/running-sum-of-1d-array/solution/

# Algorithm:
# - Define an array result.
# - Initialize the first element of result, with the first element of the input array.
# - At index i append the sum of the element nums[i] and previous running sum result[i - 1] to the result array.
# - We repeat step 3 for all indices from 1 to n-1.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = result[i - 1] + nums[i]
            
        return result


nums = [2, 6, 11, 15]
obj = Solution()
print(obj.runningSum(nums))


# Complexity Analysis:
# Time complexity: O(n) where n is the length of the input array. This is because we use a single loop that 
# iterates over the entire array to calculate the running sum.
# Space complexity: O(1) since we don't use any additional space to find the running sum. Note that we do not take 
# into consideration the space occupied by the output array.