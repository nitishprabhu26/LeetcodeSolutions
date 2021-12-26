# Approach #1 (Loop and Flip) [Accepted]

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits
            
            
n = 11
obj = Solution()
print(obj.hammingWeight(n))

# Complexity Analysis:
# Time complexity :The run time depends on the number of bits in n. Because n in this piece of code is a 
# 32-bit integer, the time complexity is O(1).
# Space complexity : O(1), since no additional space is allocated.