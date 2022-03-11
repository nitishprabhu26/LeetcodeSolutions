# Approach: Recursion

class Solution:
    def arrangeCoins(self, n: int) -> int:
        def arrange(n, row):
            if n < row:
                return row - 1
            return arrange(n - row, row + 1)
        
        return arrange(n, 1)


n = 5
obj = Solution()
print(obj.arrangeCoins(n))


# Complexity Analysis:
# Time Complexity: O(sqrt(n))
# Space Complexity: O(sqrt(n)), stack space