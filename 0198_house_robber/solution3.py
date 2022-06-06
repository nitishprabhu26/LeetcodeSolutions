# Approach 2: Dynamic Programming

# The idea here is the same as before except that instead of following a recursive approach, we will be sticking 
# with a tabular approach. 
# The recursive approach may run into trouble when the recursion stack grows too large. It may also run into 
# trouble because, for each recursive call, the compiler must do additional work to maintain the call stack 
# (function variables, etc.) which results in unwanted overhead. The dynamic programming approach is simply a 
# tabular formulation of the ideas presented above.


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0]  
        

nums = [1,2,3,1]
nums = [2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))

# Complexity Analysis:
# Time Complexity: O(N) since we have a loop from N−2 ⋯ 0 and we simply use the pre-calculated values of our 
# dynamic programming table for calculating the current value in the table which is a constant time operation.
# Space Complexity: O(N) which is used by the table. So what is the real advantage of this solution over the 
# previous solution? 
# In this case, we don't have a recursion stack. When the number of houses is large, a recursion stack can become 
# a serious limitation, because the recursion stack size will be huge and the compiler will eventually run into 
# stack-overflow problems.