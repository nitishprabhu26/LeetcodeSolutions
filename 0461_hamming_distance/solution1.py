# Approach 1: Built-in BitCounting Functions

# XOR outputs 1 if and only if the input bits are different.
# to measure the hamming distance between x and y, we can first do x XOR y operation, then we simply count the
# number of bit 1 in the result of XOR operation.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


x = 1
y = 4

obj = Solution()
print(obj.hammingDistance(x, y))


# Complexity Analysis:
# Time Complexity: O(1)
# XOR operation which takes a constant time. Then, we call the built-in bitCount function. In the worst
# scenario, the function would take O(k) time where k is the number of bits for an integer number. Since the
# Integer type is of fixed size in both Python and Java, the overall time complexity of the algorithm becomes
# constant, regardless the input numbers.
# Space Complexity: O(1), a temporary memory of constant size is consumed, to hold the result of XOR operation.
# We assume that the built-in function also takes a constant space.
