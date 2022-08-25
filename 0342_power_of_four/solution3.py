# Approach 2: Math
# OR
# https://youtu.be/xhkawOLdWzI

# The Four Basic Properties of Logs
# 1. log_b(x.y) = log_b(x) + log_b(y).
# 2. log_b(x/y) = log_b(x) - log_b(y).
# 3. log_b(x^n) = n.log_b(x).          
# 4. log_b(x)   = log_a(x) / log_a(b).

# If num is a power of four, x = 4^a, 
# Apply log_4 on both sides
# then a = log_4 x 

# WKT, log_4 (x) = [log_2(x) / log_2(4)], (or log_10() or any other base as well for the conversion)
# and also WKT log_2(4) = 2

# Therefore, a = 1/2( log_2(x) ) is an integer. 
# Hence let's simply check if log_2(x) is an even number.


import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # power of 4 cannot be a zero or a negative number
        return num > 0 and math.log2(num) % 2 == 0


# OR
# https://youtu.be/xhkawOLdWzI

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = math.log(n) / math.log(4)
        
        return res.is_integer()


n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))


# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).