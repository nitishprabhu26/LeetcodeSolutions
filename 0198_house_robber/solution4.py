# Approach 3: Optimized Dynamic Programming

# This is the exact same solution as the previous one with the exception that we will be optimizing the space 
# complexity here.

# To calculate the current value, we just need to rely on the next two consecutive values/recursive calls.
# Instead of keeping an entire table for storing these cached values, we can get by with simply keeping track of 
# the "next" two values.


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next
        

nums = [1,2,3,1]
nums = [2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))

# Complexity Analysis:
# Time Complexity: O(N) since we have a loop from N−2⋯0 and we use the precalculated values of our dynamic 
# programming table to calculate the current value in the table which is a constant time operation.
# Space Complexity: O(1) since we are not using a table to store our values. Simply using two variables will 
# suffice for our calculations.