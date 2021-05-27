# Approach : Recursion + Bit Shifts

# Intuition:
# Let's use recursion. Bases cases are sqrt{x} = x for x<2. 
# Now the idea is to decrease x recursively at each step to go down to the base cases.

# square root could be computed recursively as
# mySqrt(x) = 2 × mySqrt( x / 4)

# One could already stop here, but let's use left and right shifts, which are quite fast manipulations with bits

# x << y  that means  x * (2^y)
# x >> y  that means  x / (2^y)
 
# That means one could rewrite the recursion above as
# mySqrt(x) = mySqrt(x >> 2) << 1
# in order to fasten up the computations.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right*right > x else right
            
x = 17
obj = Solution()
print(obj.mySqrt(x))


# Complexity Analysis:

# Time complexity : O(logN).
# Space complexity : O(logN) to keep the recursion stack.