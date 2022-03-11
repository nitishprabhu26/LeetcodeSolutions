# Approach 2: Math

# If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, 
# without using any iteration.

# As a reminder, the constraint of the problem can be expressed as follows:
# k(k+1) ≤ 2N
# (simplifying this equation)
# https://leetcode.com/problems/arranging-coins/solution/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)


n = 5
obj = Solution()
print(obj.arrangeCoins(n))


# Complexity Analysis:
# Time Complexity: O(1))
# Space Complexity: O(1)