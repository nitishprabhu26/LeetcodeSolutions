# Using Recursion:

class Solution:
    def solve(self,n):
        if n==1: return True
        if n==0: return False
        else:
            if n%2==0:
                return True and self.solve(n//2)
            if n%3==0:
                return True and self.solve(n//3)
            if n%5==0:
                return True and self.solve(n//5)
        return False

    def isUgly(self, n: int) -> bool:
        return self.solve(n)


num = 11
obj = Solution()
print(obj.isUgly(num))