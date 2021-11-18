# Approach 1: Dynamic Programming

# One could rewrite recursive approach into dynamic programming one.

# Algorithm:
# - Initiate 2D array d[m][n] = number of paths. To start, put number of paths equal to 1 for the first row and the first column. 
#   For the simplicity, one could initiate the whole 2D array by ones.
# - Iterate over all "inner" cells: d[col][row] = d[col - 1][row] + d[col][row - 1].
# - Return d[m - 1][n - 1].


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col - 1]
        
        return dp[m-1][n-1]

m = 23
n = 12
obj = Solution()
print(obj.uniquePaths(m, n))



# Complexity Analysis:
# Time complexity: O(N×M).
# Space complexity: O(N×M).