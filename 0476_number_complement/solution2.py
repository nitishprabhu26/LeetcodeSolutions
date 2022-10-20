# https://leetcode.com/problems/number-complement/solution/

# Approach 2: Compute Bit Length and Construct 1-bits Bitmask

# Instead of flipping bits one by one, let's construct 1-bits bitmask and flip all the bits at once.
# Algorithm:
# - Compute bit length of the input number, length = [ log2(num) ] + 1.
# - Compute 1-bits bitmask of length l: bitmask = (1 << length) − 1.
# - Return (num ^ bitmask).


import math

class Solution:
    def findComplement(self, num):
        # n is a length of num in binary representation
        n = math.floor(math.log2(num)) + 1        
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num
        

n = 5
obj = Solution()
print(obj.findComplement(n))


# Complexity
# Time Complexity: O(1).
# Space Complexity: O(1).