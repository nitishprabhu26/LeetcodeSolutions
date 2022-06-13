# Approach : Neetcode (same as approach 2)
# https://youtu.be/g0npyaQtAQM


from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + 
                                backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]
        
        return backtrack(0, 0)
            

nums = [1,1,1,1,1]
target = 3

obj = Solution()
print(obj.findTargetSumWays(nums, target))


# Complexity Analysis
# Time complexity: O(t.n). The memo array of size O(t⋅n) has been filled just once. Here, t refers to the sum of 
# the nums array and n refers to the length of the nums array.
# Space complexity: O(t.n). The depth of the recursion tree can go up to n. The memo array contains t.n elements.
