# Approach 1: Bitwise Operators : Get the Rightmost 1-bit
# https://leetcode.com/problems/power-of-two/solution/

# Algorithm:
# Let's first discuss why x & (-x) is a way to keep the rightmost 1-bit and to set all the other bits to 0.
# Basically, that works because of two's complement. In two's complement notation (~x)+1. In other words, to compute −x one has to revert 
# all bits in x and then to add 1 to the result.
# Adding 1 to ~x in binary representation means to carry that 1-bit till the rightmost 0-bit in ~x and to set all the lower bits to zero. 
# Note, that the rightmost 0-bit in ~x corresponds to the rightmost 1-bit in x.

# In summary, -x is the same as (~x)+1. This operation reverts all bits of x except the rightmost 1-bit.
# Hence, x and -x have just one bit in common i.e. the rightmost 1-bit. That means that x & (x) would keep that rightmost 1-bit and set 
# all the other bits to 0.


# Detect Power of Two:
# So let's do x & (-x) to keep the rightmost 1-bit and to set all the others bits to zero. As discussed above, for the power of two it 
# would result in x itself, since a power of two contains just one 1-bit.
# Other numbers have more than 1-bit in their binary representation and hence for them x & (-x) would not be equal to x itself.
# Hence a number is a power of two if x & (-x) == x.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n

n = 1
n = 16
n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))

# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).