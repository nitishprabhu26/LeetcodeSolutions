# Algorithm:
# Use the golden ratio formula to calculate the Nth Fibonacci number.

class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio **n + 1) / 5 ** 0.5)


num1 = 244
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(1). Constant time complexity since we are using no loops or recursion and the time is based 
# on the result of performing the calculation using Binet's formula.
# Space complexity : O(1). The space used is the space needed to create the variable to store the golden ratio formula.