# Approach 2: Bit Manipulation: Short Language-Specific Solution
# https://leetcode.com/problems/sum-of-two-integers/editorial/
# OR
# Neetcode in JAVA - https://youtu.be/gVUrDV4tZfY

# https://leetcode.com/problems/sum-of-two-integers/editorial/
# Java solution: Java integer is a number of 32 bits. 31 bits are used for the value. The first bit is used for 
# the sign: if it's equal to 1, the number is negative, if it's equal to 0, the number is positive.

# The main goal of "two's complement" is to decrease the complexity of bit manipulations. How does Java compute 
# "two's complement" and manage 32-bits limit? Here is how:

# - After each operation we have an invisible & mask, where mask = 0xFFFFFFFF, i.e. bitmask of 32 1-bits.
# - The overflow, i.e. the situation of x > 0x7FFFFFFF (bitmask of 31 1-bits), is managed as 
#   x --> ~(x ^ 0xFFFFFFFF).

# class Solution {
#     public int getSum(int a, int b) {
#         while (b != 0) {
#             int answer = a ^ b;
#             int carry = (a & b) << 1;
#             a = answer;
#             b = carry;
#         }
#         return a;
#     }
# }


# Python Solution:
# Python has no 32-bits limit, and hence its representation of negative integers is entirely different.
# There is no Java magic by default, and if you need a magic - just do it:
# - After each operation we have an invisible & mask, where mask = 0xFFFFFFFF, i.e. bitmask of 32 1-bits.
# - The overflow, i.e. the situation of x > 0x7FFFFFFF (bitmask of 31 1-bits), is managed as 
#   x --> ~(x ^ 0xFFFFFFFF).


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff 
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)

a = 2
b = 3
obj = Solution()
print(obj.getSum(a, b))


# Complexity Analysis:
# Time complexity : O(1).
# Space complexity : O(1).
