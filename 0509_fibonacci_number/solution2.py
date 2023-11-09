# Approach 4: Iterative Bottom-Up Approach

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a = 0
        b = 1
        sum = 0
        for i in range(n - 1):
            sum = a + b
            a = b
            b = sum
        return sum

# OR
# updated

class Solution:
    def fib(self, n: int) -> int:
        if (n <= 1):
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
        
# OR

# class Solution:
#     def fib(self, n: int) -> int:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a 

num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1). 
