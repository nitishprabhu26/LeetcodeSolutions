# Approach 1: Loop Iteration


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1

n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))

# Complexity Analysis
# Time complexity : O(logb(n)). In our case that is O(log4(n)). 
# The number of divisions is given by that logarithm.
# Space complexity : O(1). We are not using any additional memory.