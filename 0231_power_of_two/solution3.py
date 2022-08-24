# Approach 2: Bitwise operators : Turn off the Rightmost 1-bit
# https://leetcode.com/problems/power-of-two/solution/


# Turn off the Rightmost 1-bit:
# Let's first discuss why x & (x - 1) is a way to set the rightmost 1-bit to zero.
# To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.
# Now AND operator: the rightmost 1-bit will be turned off because 1 & 0 = 0, and all the lower bits as well.

# Detect Power of Two:
# The solution is straightforward:
# 1. Power of two has just one 1-bit.
# 2. x & (x - 1) sets this 1-bit to zero, and hence one has to verify if the result is zero, 
#    i.e x & (x - 1) == 0.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n-1) == 0


n = 1
n = 16
# n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))


# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).