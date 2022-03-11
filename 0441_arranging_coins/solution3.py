# Approach 1: Binary Search
# OR
# Neetcode: https://youtu.be/5rHz_6s2Buw


# Naive approach might run out of time when the input becomes too large. 
# Assume that the answer is k, i.e. we've managed to complete k rows of coins. These completed rows contain in 
# total 1 + 2 + ... + k = k(k+1)/2 coins

# We could now reformulate the problem as follows:
# Find the maximum k such that, k(k+1)/2 ≤ N.


# https://leetcode.com/problems/arranging-coins/solution/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
        

# OR

# Neetcode: https://youtu.be/5rHz_6s2Buw

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            coins = mid * (mid + 1) // 2
            
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
                
        return res

n = 5
obj = Solution()
print(obj.arrangeCoins(n))


# Complexity Analysis:
# Time Complexity: O(log(n))
# Space Complexity: O(1)