# Approach 4: Bit Manipulation + Math (didnt understand %3 part)
# https://leetcode.com/problems/power-of-four/solution/
# check the explaination for the solution using the above link

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1

n = 16
# n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))

# Complexity Analysis
# Time complexity : O(1).
# Space complexity : O(1).