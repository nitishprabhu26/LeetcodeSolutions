# Approach 4: Bit Manipulation + Math
# https://leetcode.com/problems/power-of-four/solution/
# OR
# https://youtu.be/KwtRRZN6loU (solution 2)

# (Any power of 4) % 3 == 1, along with it being a power of 2
# If x is a power of two and x % 3 == 1, then x is a power of four.


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1


n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))


# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).