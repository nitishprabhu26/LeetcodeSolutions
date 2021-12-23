# https://youtu.be/UncqP2F4t_0?t=172
# Recursive

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        return n % 3 == 0 and self.isPowerOfThree( n / 3 )
        

n = 27
n = 0
# n = 9
obj = Solution()
print(obj.isPowerOfThree(n))

# Complexity Analysis
# Time complexity : O(logb(n)). 
# Space complexity : O(logb(n)).