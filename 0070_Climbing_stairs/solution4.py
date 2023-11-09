# Approach 4: Fibonacci Number

# Algorithm:
# In the above approach we have used dp array where dp[i] = dp[i-1] + dp[i-2].
# It can be easily analysed that dp[i] is nothing but i^{th} fibonacci number.
# Fib(n) = Fib(n-1) + Fib(n-2)
# Now we just have to find n^{th} number of the fibonacci series having 1 and 2 their first and second term 
# respectively, i.e. Fib(1) = 1 and Fib(2) = 2.


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        first = 1
        second = 2

        for i in range(3, n + 1):
            sum = first + second
            first = second
            second = sum

        return second


n = 38
obj = Solution()
print(obj.climbStairs(n))


# Complexity Analysis
# Time complexity : O(n). Single loop upto n is required to calculate nth fibonacci number.
# Space complexity : O(1). Constant space is used.
