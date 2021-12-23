# Log operation (method 4)
# https://youtu.be/4cqHahxFTYw?t=406
# WKT, log2(2^N) = N
# eg.1:
# i.e. log2(16) = log2(2^4) = 4
# ceil(log2(16)) == floor(log2(16))
# ceil(4) == floor(4) i.e. [4 == 4]
# eg.2:
# i.e. log2(12) = log2(2^4) = 3.584
# ceil(log2(12)) != floor(log2(12))
# ceil(3.584) != floor(3.584) i.e. [4!= 3]

# for a power of 2 number, ceil and floor of the number are the same

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n < 0:
            return False
        return math.ceil(math.log2(n)) == math.floor(math.log2(n))


n = 1
n = -16
# n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))

# Complexity analysis:
# Time complexity : O(1)
# Space complexity : O(1)
