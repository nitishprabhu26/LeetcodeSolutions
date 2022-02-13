# Naming:
# We call a position in the array a "good index" if starting at that position, we can reach the last index. 
# Otherwise, that index is called a "bad index". The problem then reduces to whether or not index 0 is a "good 
# index".

# Solution:
# This is a dynamic programming question. Usually, solving and fully understanding a dynamic programming problem 
# is a 4 step process:
# 1. Start with the recursive backtracking solution
# 2. Optimize by using a memoization table (top-down dynamic programming)
# 3. Remove the need for recursion (bottom-up dynamic programming)
# 4. Apply final tricks to reduce the time / memory complexity
# All solutions presented below produce the correct result, but they differ in run time and memory requirements.

# Approach 1: Backtracking [Time Limit Exceeded]
# This is the inefficient solution where we try every single jump pattern that takes us from the first position 
# to the last. We start from the first position and jump to every index that is reachable. We repeat the process 
# until last index is reached. When stuck, backtrack.

# refer : https://leetcode.com/problems/jump-game/solution/ for explaination

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True
            
            furthestJump = min(position + nums[position], len(nums) - 1)
            
            # for nextPosition in range(position + 1, furthestJump + 1):
            #     if canJumpFromPosition(nextPosition, nums):
            #         return True

            # One quick optimization - check the nextPosition from right to left. 
            # The theoretical worst case performance is the same, but in practice, for silly examples, the code 
            # might run faster. Intuitively, this means we always try to make the biggest jump such that we reach 
            # the end as soon as possible
            for nextPosition in range(furthestJump, position, -1):
                if canJumpFromPosition(nextPosition, nums):
                    return True
                
            return False
            
        return canJumpFromPosition(0, nums)

        
nums = [2,3,1,1,4]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,
        9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
obj = Solution()
print(obj.canJump(nums))


# Complexity Analysis:

# Time complexity : O(2^n). There are 2^n (upper bound) ways of jumping from the first position to the last, where 
# n is the length of array nums.
# Space complexity : O(n). Recursion requires additional memory for the stack frames.