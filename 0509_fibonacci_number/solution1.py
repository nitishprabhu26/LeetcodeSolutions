# Approach 1: Recursion

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-2) + self.fib(n-1)


num1 = 5
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(2^N).
# Space complexity : O(N). We need space proportionate to N to account for the max size of the stack, in memory.
# This stack keeps track of the function calls to fib(N).
