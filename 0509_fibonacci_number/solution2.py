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

num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1). 
