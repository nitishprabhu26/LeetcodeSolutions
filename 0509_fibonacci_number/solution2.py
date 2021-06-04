class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a = 0
        b = 1
        sum = 0
        for i in range(n-1):
            sum = a+b
            a = b
            b = sum
        return sum

# class Solution:
#     def fib(self, n: int) -> int:
#         a,b = 0,1
#         for _ in range(n):
#             a, b = b, a+b
#         return a 

num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1). 
