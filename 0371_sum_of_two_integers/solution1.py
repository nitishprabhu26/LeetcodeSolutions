# Approach 1: Bit Manipulation: Easy and Language-Independent
# https://leetcode.com/problems/sum-of-two-integers/solution/ (check explaination)


# Reduce the Number of Use Cases:
# First of all, there are too many use cases here: both a and b could be positive or negative, abs(a) could be 
# greater or less than abs(b). In total, that results in 2 × 2 × 2 = 8 use cases.
# Let's start by reducing the problem down to two simple cases:
# - Sum of two positive integers: x + y, where x > y.
# - Difference of two positive integers: x - y, where x > y.


# Algorithm:

# Simplify problem down to two cases: sum or subtraction of two positive integers: x ± y, where x > y. Save down 
# the sign of the result.

# If one has to compute the sum:
# - While carry is nonzero: y != 0:
#   -   Current answer without carry is XOR of x and y: answer = x ^ y.
#   -   Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
#   -   Job is done, prepare the next loop: x = answer, y = carry.
# - Return x * sign.

# If one has to compute the difference:
# - While borrow is nonzero: y != 0:
#   -   Current answer without borrow is XOR of x and y: answer = x ^ y.
#   -   Current borrow is left-shifted AND of NOT x and y: borrow = ((~x) & y) << 1.
#   -   Job is done, prepare the next loop: x = answer, y = borrow.
# - Return x * sign.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                # print(answer)
                borrow = ((~x) & y) << 1
                # print(borrow)
                x, y = answer, borrow
        
        return x * sign



# This solution could be written a bit shorter in Python:
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign


# test case to understand difference (else case)
a = 9
b = -2
obj = Solution()
print(obj.getSum(a, b))


# Complexity Analysis:
# Time complexity: O(1) because each integer contains 32 bits.
# Space complexity: O(1) because we don't use any additional data structures.