# Approach 3: Brian Kernighan's Algorithm
# after encountering the first bit of one at the rightmost position, it would be more efficient if we just
# jump at the next bit of one, skipping all the zeros in between.
# When we do AND bit operation between number and number-1, the rightmost bit of '1' in the original number
# would be cleared.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor-1)
        return distance


x = 1
y = 4

obj = Solution()
print(obj.hammingDistance(x, y))


# Complexity Analysis:
# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant
# time. For an Integer of 32 bit, the algorithm would take at most 32 iterations.
# However, this algorithm would require less iterations than the bit shift approach
# Space Complexity: O(1), a constant size of memory is used, regardless the input.
