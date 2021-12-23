# Bit shift (method 3)
# https://youtu.be/4cqHahxFTYw?t=255
# keep shifting bits of 'n' until we find 1 at the LSB(Least Significant Bit), break when we find 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n > 1 and (n & 1) == 0:
            # print(n)
            n >>= 1
        return n == 1


n = 1
n = 16
# n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))

# Complexity analysis:
# Time complexity : O(logN). value of n is right shifted (arithmetic shift). 
# equivalent to removing one LSB at a time
# Space complexity : O(1)
