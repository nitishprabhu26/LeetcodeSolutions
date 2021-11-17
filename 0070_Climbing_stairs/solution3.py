# Approach 3: Dynamic Programming

# Algorithm:
# optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve 
# this problem.

# One can reach i th step in one of the two ways:
# 1. Taking a single step from (i−1) th step.
# 2. Taking a step of 2 from (i−2) th step.

# So, the total number of ways to reach i^{th} is equal to sum of ways of reaching (i-1)^{th} step and ways of reaching (i-2)^{th} step.
# Let dp[i] denotes the number of ways to reach on i^{th} step:
# dp[i]=dp[i-1]+dp[i-2]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
n = 38
obj = Solution()
print(obj.climbStairs(n))


# Complexity Analysis:
# Time complexity : O(n). Single loop upto n.
# Space complexity : O(n). dp array of size n is used.
