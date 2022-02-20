# Approach 2: Dynamic Programming
# https://leetcode.com/problems/maximum-product-subarray/solution/ (check animation example)

# Intuition:
# Rather than looking for every possible subarray to get the largest product, we can scan the array and solve 
# smaller subproblems.
# Let's see this problem as a problem of getting the highest combo chain. The way combo chains work is that they 
# build on top of the previous combo chains that you have acquired. The simplest case is when the numbers in nums 
# are all positive numbers. In that case, you would only need to keep on multiplying the accumulated result to get 
# a bigger and bigger combo chain as you progress.

# However, two things can disrupt your combo chain:
# - Zeros
# - Negative numbers

# Zeros will reset your combo chain. A high score which you have achieved will be recorded in placeholder result. 
# You will have to restart your combo chain after zero. If you encounter another combo chain which is higher than 
# the recorded high score in result, you just need to update the result.

# Negative numbers are a little bit tricky. A single negative number can flip the largest combo chain to a very 
# small number. This may sound like your combo chain has been completely disrupted but if you encounter another 
# negative number, your combo chain can be saved. Unlike zero, you still have a hope of saving your combo chain 
# as long as you have another negative number in nums.

# While going through numbers in nums, we will have to keep track of the maximum product up to that number (we 
# will call max_so_far) and minimum product up to that number (we will call min_so_far). The reason behind keeping 
# track of max_so_far is to keep track of the accumulated product of positive numbers. The reason behind keeping 
# track of min_so_far is to properly handle negative numbers.

# max_so_far is updated by taking the maximum value among:
# - Current number:
# This value will be picked if the accumulated product has been really bad (even compared to the current number). 
# This can happen when the current number has a preceding zero (e.g. [0,4]) or is preceded by a single negative 
# number (e.g. [-3,5]).
# - Product of last max_so_far and current number:
# This value will be picked if the accumulated product has been steadily increasing (all positive numbers).
# - Product of last min_so_far and current number:
# This value will be picked if the current number is a negative number and the combo chain has been disrupted by 
# a single negative number before.

# min_so_far is updated in using the same three numbers except that we are taking minimum among the above three 
# numbers.

import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
                
        # optional
        if math.prod(nums) > 0:
            return math.prod(nums)

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result    

nums = [3,4,5,1,2]
obj = Solution()
print(obj.maxProduct(nums))


# Complexity Analysis
# Time complexity : O(N) where N is the size of nums. The algorithm achieves linear runtime since we are going 
# through nums only once.
# Space complexity : O(1) since no additional space is consumed rather than variables which keep track of the 
# maximum product so far, the minimum product so far, current variable, temp variable, and placeholder variable 
# for the result.