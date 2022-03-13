# Approach 2: Fast Power Algorithm Recursive
# https://leetcode.com/problems/powx-n/solution/

# Intuition:
# Assuming we have got the result of x^n, how can we get x ^ (2 ∗ n)? 
# Obviously we do not need to multiply x for another n times. 
# Using the formula (x ^ n)^ 2 = x ^ (2 ∗ n), we can get x ^ (2 ∗ n) at the cost of only one computation. 
# Using this optimization, we can reduce the time complexity of our algorithm.


# Algorithm:
# Assume we have got the result of x^(n/2), and now we want to get the result of x^n. 
# Let A be result of x^(n/2), we can talk about x^n based on the parity of n respectively. 
# If n is even, we can use the formula (x ^ n)^ 2 = x ^ (2 ∗ n) to get x ^ n = A * A.
# If n is odd, then A * A = x ^ (n - 1). 
# Intuitively, We need to multiply another x to the result, so x ^ n = A * A * x.

# We call this method "Fast Power", because we only need at most O(logn) computations to get x^n.
 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1.0
            
            half = fastPow(x, n//2)
            
            # n is even case
            if n % 2 == 0:
                return half * half
            # n is odd case
            else:
                return half * half * x
                
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        
        return fastPow(x, N)


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
