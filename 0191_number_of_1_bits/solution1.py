class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    

n = 0b11111111111111111111111111111101
obj = Solution()
print(obj.hammingWeight(n))


# Complexity Analysis:
# Time Complexity: O(n).
# bin() method - O(log n), where 'n' is the integer that is being converted.
# This method needs to iterate through the bits of the integer to create the binary representation. The number 
# of bits in the binary representation is proportional to the logarithm (base 2) of the integer value.
# count() method - O(n), where 'n' is the length of the iterable. 
# Space Complexity: O(1).