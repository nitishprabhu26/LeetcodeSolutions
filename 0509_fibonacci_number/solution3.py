# Approach 2: Bottom-Up Approach using Memoization
# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer 
# programs by storing the results of expensive function calls and returning the cached result when the same 
# inputs occur again.

# Intuition:
# Improve upon the recursive approach by using iteration, still solving for all of the sub-problems and 
# returning the answer for N, using already computed Fibonacci values. While using a bottom-up approach, we 
# can iteratively compute and store the values, only returning once we reach the result.

# Algorithm:
# - If N is less than or equal to 1, return N
# - Otherwise, iterate through N, storing each computed answer in an array along the way.
# - Use this array as a reference to the 2 previous numbers to calculate the current Fibonacci number.
# - Once we've reached the last number, return it's Fibonacci number.


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.memoize(n)

    def memoize(self, N):
        cache = {0: 0, 1: 1}

        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]


# OR
# updated

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        cache = [0] * (n + 1)
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]
        

num1 = 2
obj = Solution()
print(obj.fib(num1))

# Complexity Analysis:
# Time complexity : O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored 
# for O(1) access later on.
# Space complexity : O(N). The size of the data structure is proportionate to N.
