# Approach 3: Mathematics
# We can use mathematics as follows

# n = 3^i
# apply log on both sides
# log3(n) = i.log3(3)
# i = log3(n)
# therefore i = [ logb(n) / logb(3)] 
# n is a power of three if and only if i is an integer. In Java, we check if a number is an integer by taking 
# the decimal part (using % 1) and checking if it is 0.

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        return ( math.log10(n) / math.log10(3) ) % 1 == 0


n = 27
# n = 0
# n = 9
obj = Solution()
print(obj.isPowerOfThree(n))

# Complexity Analysis
# Time complexity : depends on the language. in python may be O(1) since it could be just a lookup
# Space complexity : O(1). We are not using any additional memory.