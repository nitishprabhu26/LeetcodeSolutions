# Approach 1: Brute Force
# for all solutions:
# https://www.youtube.com/watch?v=Y0lT9Fck7qI

# We take all possible step combinations i.e. 1 and 2, at every step. At every step we are calling the function 
# climbStairs for step 1 and 2, and return the sum of returned values of both functions.
# climbStairs(i,n) = climbStairs(i + 1, n) + climbStairs(i + 2, n)
# where i defines the current step and n defines the destination step.       


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_stairs(0, n)
    
    def climb_stairs(self, i, n):
        if i > n:
            return 0
        
        if i == n:
            return 1
        
        return self.climb_stairs(i+1, n)+ self.climb_stairs(i+2, n)


n = 5
obj = Solution()
print(obj.climbStairs(n))


# Complexity Analysis:
# Time complexity : O(2^n). Size of recursion tree will be 2^n. (2 decision at each node)
# where n is the length of the decision tree (longest path)
# Space complexity : O(n). The depth of the recursion tree can go upto n.
