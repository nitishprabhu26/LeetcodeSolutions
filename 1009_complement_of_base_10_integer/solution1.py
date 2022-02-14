# Prerequisites:
# XOR of zero and a bit results in that bit
# 0 ⊕ x = x
# XOR of one and a bit flips that bit
# 1 ⊕ x = 1 − x

# There are two standard ways to solve the problem:
# - To move along the number and flip bit by bit.
# - To construct 1-bits bitmask which has the same length as the input number, and to get the answer as 
# bitmask - num or bitmask ^ num.
# For example, for num = 5 = (101)2 the bitmask is bitmask=(111)2, and the 
# complement number is bitmask ⊕ num = (010)2 = 2.


# Approach 1: Flip Bit by Bit
# Initiate 1-bit variable which will be used to flip bits one by one. Set it to the smallest register bit = 1.
# Initiate the marker variable which will be used to stop the loop over the bits todo = num.
# Loop over the bits. While todo != 0:
# Flip the current bit: num = num ^ bit.
# Prepare for the next run. Shift flip variable to the left and todo variable to the right.
# Return num.


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        todo, bit = N, 1
        while todo:
            # flip current bit
            N = N ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return N
        
n = 5
obj = Solution()
print(obj.bitwiseComplement(n))

# Complexity
# Time Complexity: O(1), since we're doing not more than 32 iterations here.
# Space Complexity: O(1).