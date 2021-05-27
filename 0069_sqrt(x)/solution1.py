import math
class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(x**0.5)
        return math.trunc(pow(x,0.5))
#round() - round Python numbers to the nearest full integer
#math.floor() - Round down to the next integer
# math.ceil() - Round up to the next integer
            
x = 8
obj = Solution()
print(obj.mySqrt(x))
