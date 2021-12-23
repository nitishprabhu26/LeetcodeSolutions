# Approach 4: Integer Limitations (may be only for java since we know max int value in java and that value is 
# divisible by 3 or power if 3)
# https://youtu.be/UncqP2F4t_0?t=405
# https://leetcode.com/problems/power-of-three/solution/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and pow(3, 32) % n == 0

n = 27
n = 0
n = 9
obj = Solution()
print(obj.isPowerOfThree(n))

# Complexity Analysis
# Time complexity : O(1). We are only doing one operation.
# Space complexity : O(1). We are not using any additional memory.