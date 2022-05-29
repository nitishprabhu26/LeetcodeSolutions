# Approach #4 Gauss' Formula [Accepted]
# OR
# Neetcode:(using only 1 loop instead of 2)
# https://youtu.be/WnPLSRLSANE

# Formula to find sum of first 'n' natural numbers:
# Gauss' Formula: sum = [n.(n+1)]//2

# Algorithm:
# We can compute the sum of nums in linear time, and by Gauss' formula, we can compute the sum of the first n 
# natural numbers in constant time. Therefore, the number that is missing is simply the result of Gauss' formula 
# minus the sum of nums, as nums consists of the first n natural numbers minus some number.


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# OR
# Neetcode:


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))


# Complexity Analysis
# Time complexity : O(n). 
# Although Gauss' formula can be computed in O(1) time, summing nums costs us O(n) time, so the algorithm is 
# overall linear.
# Space complexity : O(1).
# This approach only pushes a few integers around, so it has constant memory usage.