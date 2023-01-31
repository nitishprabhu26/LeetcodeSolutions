# Possible Solutions: Space vs Performance Optimisation
# https://leetcode.com/problems/n-th-tribonacci-number/solution/
 
# Simple Recursion : [Time Limit Exceeded]
# Simple recursion like tribonacci(k) = tribonacci(k - 1) + tribonacci(k - 2) + tribonacci(k - 3) is out of 
# consideration here because it will result in exponential time complexity 3^N.


class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n else 0
        
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        

n = 30
obj = Solution()
print(obj.tribonacci(n))


# Complexity Analysis:
# Time complexity : O(3^N).
# Space complexity : O(N). We need space proportional to N to account for the max size of the stack, in memory.