# Approach 2: Bit Shift (Kevin Naughton Jr.)
# https://youtu.be/oGU1At1GFvc

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x > 0 or y > 0:
            # num % 2 tells if last bit is present or not (gives the last bit) 
            # (checks is number is even or odd)
            result += (x % 2) ^ (y % 2)
            x >>= 1
            y >>= 1
        return result


x = 1
y = 4

obj = Solution()
print(obj.hammingDistance(x, y))


# Complexity Analysis:
# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant
# time. For an Integer of 32 bit, the algorithm would take at most 32 iterations.
# Space Complexity: O(1), a constant size of memory is used, regardless the input.
