# Approach 0: Brute Force - Recursive approach
# https://leetcode.com/problems/unique-paths/solution/

# Since robot can move either down or right, there is only one path to reach the cells in the first row: 
# right->right->...->right.
# The same is valid for the first column, though the path here is down->down-> ...->down.
# What about the "inner" cells (m, n)? 
# To such cell one could move either from the cell on the left (m, n - 1), or from the cell above (m - 1, n). 
# That means that the total number of paths to move into (m, n) cell is 
# uniquePaths(m - 1, n) + uniquePaths(m, n - 1).       

# This solution is not fast enough to pass all the testcases, though it could be used as a starting point for 
# the DP solution.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


m = 7
n = 4
obj = Solution()
print(obj.uniquePaths(m, n))