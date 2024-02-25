# Approach #2 (Bit Manipulation Trick) [Accepted]

class Solution:
    def hammingWeight(self, n: int) -> int:
        distance = 0
        while n:
            distance += 1
            # remove the rightmost bit of '1'
            n = n & (n-1)
        return distance
            
            
n = 0b11
obj = Solution()
print(obj.hammingWeight(n))

# Complexity Analysis:
# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant
# time. For an Integer of 32 bit, the algorithm would take at most 32 iterations.
# However, this algorithm would require less iterations than the bit shift approach
# Space Complexity: O(1), a constant size of memory is used, regardless the input.