# Approach 3: Bit Manipulation
# https://leetcode.com/problems/power-of-four/solution/ (check images)

# Let's first check if num is a power of two: x > 0 and x & (x - 1) == 0.
# Now the problem is to distinguish between even powers of two (when x is a power of four) and odd powers of 
# two (when x is not a power of four). In binary representation both cases are single 1-bit followed by zeros.
# What is the difference? 
# In the first case (power of four), 1-bit is at even position: bit 0, bit 2, bit 4, etc. 
# In the second case, at odd position.
# Hence power of four would make a zero in a bitwise AND with number (101010...10)_2:
# 4^a ∧ (101010...10)_2 == 0


# Approach 3: Bit Manipulation
# OR
# https://youtu.be/KwtRRZN6loU (solution 3)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0


# OR 
# log(n) solution
# https://youtu.be/KwtRRZN6loU (solution 1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        # Right shift until num becomes equal to 1
        # calculate number of right shifts we made, i.e. count
        # then left shift that many number of times
        # then check if we get back the same number
        num = n
        count = 0
        while num > 1:
            num >>= 2
            count += 2
            
        return (num << count) == n
        

n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))


# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).