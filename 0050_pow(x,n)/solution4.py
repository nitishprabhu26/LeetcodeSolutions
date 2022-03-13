# Approach : Neetocde
# https://youtu.be/g9YQyYi4IQQ


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def helper(x, n):
            if n == 0:
                return 1
            
            res = helper(x, n//2)
            res = res * res
            
            return x * res if n % 2 else res
        
        # x^(-n) = 1/(x^n)
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res


# x = 2.00000
# n = 10
x = 2.00000
n = -2
obj = Solution()
print(obj.myPow(x, n))


# Complexity Analysis:
# Time complexity : O(logn). Each time we apply the formula (x ^ n)^ 2 = x ^ (2 ∗ n), n is reduced by half. 
# Thus we need at most O(logn) computations to get the result.
# Space complexity : O(log n). For each computation, we need to store the result of x ^ (n / 2). We need to do 
# the computation for O(logn) times, so the space complexity is O(logn).
