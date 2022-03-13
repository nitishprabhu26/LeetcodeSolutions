# Approach 1: Brute Force [Time Limit Exceeded]
# https://leetcode.com/problems/powx-n/solution/

# Just simulate the process, multiply x for n times.
# If n < 0, we can substitute x, n with (1/x) , (−n) to make sure n ≥ 0.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        
        ans = 1
        for i in range(N):
            ans = ans * x
        return ans


# x = 2.00000
# n = 10
x = 2.00000
n = -2
obj = Solution()
print(obj.myPow(x, n))


# Complexity Analysis:
# Time complexity : O(n). We will multiply x for n times.
# Space complexity : O(1). We only need one variable to store the final product of x.
