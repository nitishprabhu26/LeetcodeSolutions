# Approach 2: Recursion with Memoization (i.e. caching the result)

# Algorithm:
# In the previous approach we are redundantly calculating the result for every step. Instead, we can store the 
# result at each step in memo array and directly returning the result from the memo array whenever that function 
# is called again.
# In this way we are pruning recursion tree with the help of memo array and reducing the size of recursion tree 
# upto n.


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n)
        return self.climb_stairs(0, n, memo)
    
    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0
        
        if i == n:
            return 1

        if memo[i] > 0:
            return memo[i]
        
        memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)

        return memo[i]


n = 38
obj = Solution()
print(obj.climbStairs(n))


# Complexity Analysis:
# Time complexity : O(n). Size of recursion tree can go upto n. (AFTER ELIMINATING ALL REPEATED WORK USING MEMO 
# ARRAY)
# we are only solving each subproblem once
# where n is the length of the decision tree (longest path)
# Space complexity : O(n). The depth of recursion tree can go upto n.