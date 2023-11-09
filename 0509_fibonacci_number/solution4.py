# Approach 3: Top-Down Approach using Memoization

# Intuition:
# Solve for all of the sub-problems, use memoization to store the pre-computed answers, then return the answer 
# for N. We will leverage recursion, but in a smarter way by not repeating the work to calculate existing values.


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        self.cache = {0: 0, 1: 1}
        return self.memoize(n)

    def memoize(self, N):
        if N in self.cache.keys():
            return self.cache[N]

        self.cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)

# OR
# updated

class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]
        

num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored
# for O(1) access later on.
# Space complexity : O(N). The size of the stack in memory is proportionate to N.
