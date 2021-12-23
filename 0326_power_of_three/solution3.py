# Approach 2: Base Conversion
# https://youtu.be/UncqP2F4t_0?t=237
# In Base 10, all powers of 10 start with the digit '1' and then are followed only by 0 (e.g. 10, 100, 1000). 
# This is true for other bases and their respective powers. For instance in base 2, the representations of 
# 10(base2), 100(base2) and 1000(base2) are 2(base10), 4(base10) and 8(base10) respectively. 
# Therefore if we convert our number to base 3 and the representation is of the form 100...0, then the number 
# is a power of 3.
# Implementation:
# All we need to do is convert [1] the number to base 3 and check if it is written as a leading 1 followed by 
# all 0.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        
        # conversion to base 3 (numpy has a method)
        nbase3 = ""
        
        # if n = 1 case where nbase3 = "1"
        if n == 1:
            nbase3 = "1"
        elif n == 2:
            nbase3 = "0"
        else:
            while n:
                nbase3 = str( n % 3) + nbase3
                n //= 3
        
        # check if all the indexes are '0' except for the first index
        for i in range(1, len(nbase3)):
            if nbase3[i] != '0':
                return False

        return nbase3[0] == '1'


n = 27
n = 0
n = 9
obj = Solution()
print(obj.isPowerOfThree(n))

# Complexity Analysis
# Time complexity : O(logb(n)).
# Space complexity : O(logb(n)).