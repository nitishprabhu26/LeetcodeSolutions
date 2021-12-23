# Approach 1: Loop Iteration
# https://youtu.be/GNb8vSyw-WE
# One simple way of finding out if a number n is a power of a number b is to keep dividing n by b as long as 
# the remainder is 0.
# n = b^x
# n = b × b × … × b
# Hence it should be possible to divide n by b, 'x' times, every time with a remainder of 0 and the end result 
# to be 1.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

# we dont need the condition for n == 0
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         while n >= 2:
#             if n % 3 != 0: return False
#             n /= 3
#         return n == 1

n = 27
n = 0
n = 9
obj = Solution()
print(obj.isPowerOfThree(n))

# Complexity Analysis
# Time complexity : O(logb(n)). In our case that is O(log3(n)). 
# The number of divisions is given by that logarithm.
# Space complexity : O(1). We are not using any additional memory.