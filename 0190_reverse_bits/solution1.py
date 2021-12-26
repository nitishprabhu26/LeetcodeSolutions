# Approach 1: Bit by Bit
# &&
# Neetcode:
# https://youtu.be/UcoN6UjAI64

# Intuition:
# To retrieve the right-most bit in an integer n, one could either apply the modulo operation (i.e. n % 2) or 
# the bit AND operation (i.e. n & 1). 
# In order to combine the results of reversed bits (e.g. 2^a, 2^b), one could either use the addition operation
# (i.e. 2^a + 2^b) or again the bit OR operation (i.e. 2^a | 2^b)

# Algorithm
# The key idea is that for a bit that is situated at the index i, after the reversion, its position should be 
# 31-i (note: the index starts from zero).

class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res
            
# &&

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             bit = (n >> i) & 1
#             res = res | (bit << (31-i))
#         return res


n = 43261596
obj = Solution()
print(obj.reverseBits(n))

# Complexity Analysis:
# Time Complexity: O(1). Though we have a loop in the algorithm, the number of iteration is fixed regardless 
# the input, since the integer is of fixed-size (32-bits) in our problem.
# Space Complexity: O(1), since the consumption of memory is constant regardless the input