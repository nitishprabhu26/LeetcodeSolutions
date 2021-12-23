# obvious O(logN) time solution and also in the video(method1)
# https://youtu.be/4cqHahxFTYw

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

# multiply 'i' by 2 until 'i' is not less than n
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         i = 1
#         while i < n:
#             i *= 2
#         return i == n

n = 1
n = 16
# n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))

# Complexity analysis:
# Time complexity : O(logN). value of n is divided by 2 every iteration until we get an odd number
# Space complexity : O(1)