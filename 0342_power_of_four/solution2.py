# Approach 1: Brute Force + Precomputations
# Let's precompute all possible answers

# Input number is known to be signed 32 bits integer, i.e. x <= 2^{31} - 1. Hence the max power of four to be 
# considered is [log_4 (2^{31} - 1)] = 15.Let's precompute all possible answers, and then during the runtime 
# just check if input number is in the list of answers.

class Powers:
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]

class Solution:
    p = Powers()
    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums

n = 16
n = 5
# n = 1
obj = Solution()
print(obj.isPowerOfFour(n))

# Complexity Analysis
# Time complexity: O(1).
# Space complexity: O(1).