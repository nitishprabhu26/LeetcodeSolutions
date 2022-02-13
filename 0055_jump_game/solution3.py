# Approach 3: Dynamic Programming Bottom-up [Time Limit Exceeded]

# Top-down to bottom-up conversion is done by eliminating recursion. In practice, this achieves better performance 
# as we no longer have the method stack overhead and might even benefit from some caching. More importantly, this 
# step opens up possibilities for future optimization. The recursion is usually eliminated by trying to reverse 
# the order of the steps from the top-down approach.
# The observation to make here is that we only ever jump to the right. This means that if we start from the right 
# of the array, every time we will query a position to our right, that position has already be determined as being 
# GOOD or BAD. This means we don't need to recurse anymore, as we will always hit the memo table.

# refer : https://leetcode.com/problems/jump-game/solution/ for explaination

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # memoization - all elements of the memo table are UNKNOWN, except for the last one, which is (trivially) 
        # GOOD (it can reach itself)
        memo = ['UNKNOWN'] * len(nums)
        memo[len(nums) - 1] = 'GOOD'
        
            
        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == 'GOOD':
                    memo[i] = 'GOOD'
                    break
            
        return memo[0] == 'GOOD'

        
nums = [2,3,1,1,4]
obj = Solution()
print(obj.canJump(nums))


# Complexity Analysis:
# Time complexity : O(n^2). For every element in the array, say i, we are looking at the next nums[i] elements to 
# its right aiming to find a GOOD index. nums[i] can be at most n, where n is the length of array nums.
# Space complexity : O(n). This comes from the usage of the memo table.