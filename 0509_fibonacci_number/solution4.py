# Approach 3: Top-Down Approach using Memoization

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        self.cache = {0: 0, 1: 1}
        return self.memoize(n)

    def memoize(self, N):
        if N in self.cache.keys():
            return self.cache[N]

        self.cache[N] = self.memoize(N-1)+self.memoize(N-2)
        return self.memoize(N)


num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored
# for O(1) access later on.
# Space complexity : O(N). The size of the stack in memory is proportionate to N.
