# Converting to str(bin(n))
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        for i in str(bin(n)):
            if i == "1":
                count += 1
        return True if count == 1 else False


# OR
        
# Counting Set bits (method 2) (exactly same)
# https://youtu.be/4cqHahxFTYw?t=121

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        x = 1
        while (x <= n):
            if x & n:
                count += 1
            x <<= 1
        return count == 1

        
# Counting Set bits (method 2) (not exactly same)
# https://youtu.be/4cqHahxFTYw?t=121

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while (n > 0):
            count += n & 1
            n >>= 1
        return count == 1


n = 1
n = 16
# n = 3
obj = Solution()
print(obj.isPowerOfTwo(n))


# Complexity analysis:
# Time complexity : O(logN). value of n is right shifted (arithmetic shift). This is equivalent to removing one 
# LSB at a time
# Space complexity : O(1)
