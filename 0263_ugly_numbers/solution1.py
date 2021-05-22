# Similar question: Geeks for Geeks: https://www.geeksforgeeks.org/ugly-numbers/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n=n//i
        return n==1


num = 10
obj = Solution()
print(obj.isUgly(num))
