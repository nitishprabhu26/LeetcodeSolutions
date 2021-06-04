# Approach 2: Bottom-Up Approach using Memoization
# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs 
# by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.memoize(n)

    def memoize(self, N):
        cache = {0: 0, 1: 1}

        for i in range(2, N+1):
            cache[i] = cache[i-1]+cache[i-2]

        return cache[N]


num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored 
# for O(1) access later on.
# Space complexity : O(N). The size of the data structure is proportionate to N.
