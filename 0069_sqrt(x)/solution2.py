# Linear approach:

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        ans=0
        for i in range(0,x//2+1):
            if i*i <= x:
                ans=i
            else:
                return i-1
        return ans
            
x = 6
obj = Solution()
print(obj.mySqrt(x))
