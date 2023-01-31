# Approach 1: Space Optimisation : Dynamic Programming
# - If n < 3 the answer is obvious.
# - Otherwise initiate the first three numbers x = 0, y = z = 1 and proceed to the loop of n - 2 steps. At each 
# step:
#   -   Replace x by y.
#   -   Replace y by z.
#   -   Replace z by x + y + z.
# - Return z.


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z
        

n = 4
obj = Solution()
print(obj.tribonacci(n))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : constant space to keep the last three Fibonacci numbers.
