# https://leetcode.com/problems/complement-of-base-10-integer/solution/

# Approach 2: Compute Bit Length and Construct 1-bits Bitmask

# Instead of flipping bits one by one, let's construct 1-bits bitmask and flip all the bits at once.
# Algorithm:
# - Compute bit length of the input number, length = [ log2(num) ] + 1.
# - Compute 1-bits bitmask of length l: bitmask = (1 << length) − 1.
# - Return (num ^ bitmask).


import math

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        # length is a length of N in binary representation
        length = math.floor( math.log2(N) ) + 1        
        # bitmask has the same length as N and contains only ones 1...1
        bitmask = (1 << length) - 1
        # flip all bits
        return bitmask ^ N
        

n = 5
obj = Solution()
print(obj.bitwiseComplement(n))


# Complexity
# Time Complexity: O(1).
# Space Complexity: O(1).