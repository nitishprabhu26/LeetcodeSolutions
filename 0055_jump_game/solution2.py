# Approach 2: Dynamic Programming Top-down [Time Limit Exceeded]

# Top-down Dynamic Programming can be thought of as optimized backtracking. It relies on the observation that once 
# we determine that a certain index is good / bad, this result will never change. This means that we can store the 
# result and not need to recompute it every time.
# Therefore, for each position in the array, we remember whether the index is good or bad. Let's call this array 
# memo and let its values be either one of: GOOD, BAD, UNKNOWN. This technique is called memoization


# Algorithm:

# Initially, all elements of the memo table are UNKNOWN, except for the last one, which is (trivially) GOOD 
# (it can reach itself)
# Modify the backtracking algorithm such that the recursive step first checks if the index is known (GOOD / BAD)
#    1. If it is known then return True / False
#    2. Otherwise perform the backtracking steps as before
# Once we determine the value of the current index, we store it in the memo table

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # memoization - all elements of the memo table are UNKNOWN, except for the last one, which is (trivially) GOOD (it can reach itself)
        memo = ['UNKNOWN'] * len(nums)
        memo[len(nums) - 1] = 'GOOD'
        
        def canJumpFromPosition(position, nums):
            if memo[position] != 'UNKNOWN':
                return True if memo[position] == 'GOOD' else False
            
            furthestJump = min(position + nums[position], len(nums) - 1)
            
            for nextPosition in range(position + 1, furthestJump + 1):
                if canJumpFromPosition(nextPosition, nums):
                    memo[position] = 'GOOD'
                    return True
            
            memo[position] = 'BAD'
            return False
            
        return canJumpFromPosition(0, nums)

        
nums = [2,3,1,1,4]
# RecursionError: maximum recursion depth exceeded for a large input [Time Limit Exceeded]
obj = Solution()
print(obj.canJump(nums))


# Complexity Analysis:

# Time complexity : O(n^2). For every element in the array, say i, we are looking at the next nums[i] elements 
# to its right aiming to find a GOOD index. nums[i] can be at most n, where n is the length of array nums.
# Space complexity : O(2n)=O(n). First n originates from recursion. Second n comes from the usage of the 
# memo table.