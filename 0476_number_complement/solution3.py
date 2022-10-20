# https://leetcode.com/problems/number-complement/solution/

# Approach 3: Built-in Functions to Construct 1-bits Bitmask
# Approach 2 could be rewritten with the help of built-in functions: bit_length in Python


class Solution:
    def findComplement(self, num):
        return (1 << num.bit_length()) - 1 - num
        
        
n = 5
obj = Solution()
print(obj.findComplement(n))


# Complexity
# Time Complexity: O(1) because one deals here with integers of not more than 32 bits.
# Space Complexity: O(1).


# Extras: Bit length of a positive integer in Python:

# 1 = 0b1 -> 1
# 5 = 0b101 -> 3
# 10 = 0b1010 -> 4

# Method 1:
# >>> a = 100
# >>> a.bit_length()
# 7

# Method 2:
# Positive numbers:
# >>> len(bin(1000))-2
# 10
# >>> len(bin(1)[2:])
# 1

# Negative numbers:
# >>> len(bin(-1000))-3
# 10
# >>> len(bin(-1)[3:])
# 1

# Method 3:
# def bit_length(n): # return the bit size of a non-negative integer
#     bits = 0
#     while n >> bits: bits += 1
#     return bits