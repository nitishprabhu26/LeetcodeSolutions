# Approach 2: Math
# If num is a power of four,
# x = 4^a, 
# then a = log_4 x 
# = 1/2( log_2 x ) is an integer. 
# Hence let's simply check if log_2 x is an even number.

import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log2(num) % 2 == 0

n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))

# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).