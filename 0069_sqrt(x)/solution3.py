# Linear approach - using while:

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         ans=0
#         i=0
#         while True:
#             if i*i<=x:
#                 ans=i
#             else:
#                 return i-1
#             i+=1


class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        i=0
        while True:
            if i*i<x:
                ans=i
            elif i*i==x:
                return i
            else:
                return i-1
            i+=1
            
x = 10
obj = Solution()
print(obj.mySqrt(x))
