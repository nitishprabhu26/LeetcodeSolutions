# Approach 2: Bit Shift
# In order to count the number of bit 1, we could shift each of the bit to either the leftmost or the rightmost 
# position and then check if the bit is one or not.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance


x = 1
y = 4

obj = Solution()
print(obj.hammingDistance(x, y))


# Complexity Analysis:
# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant 
# time. For an Integer of 32 bit, the algorithm would take at most 32 iterations.
# Space Complexity: O(1), a constant size of memory is used, regardless the input.
