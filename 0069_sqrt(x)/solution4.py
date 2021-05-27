# Approach: Binary Search

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left = 2
        # sqrt of a number is less than half of the number
        right = x//2
        while left <= right:
            # mid = (left+right)//2
            # overflow condition - integer value overflow if x is ma number, 2^31
            # to prevent 32 bit integer overflow
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid -1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right
            
x = 17
obj = Solution()
print(obj.mySqrt(x))



# Algorithm:

# If x < 2, return x.
# Set the left boundary to 2, and the right boundary to x / 2.

# While left <= right:
# Take mid = (left + right) / 2 as a guess. Compute mid * mid and compare it with x:
# If mid * mid > x, move the right boundary right = mid -1
# Else, if mid * mid < x, move the left boundary left = mid + 1
# Otherwise mid * mid == x, the integer square root is here, let's return it

# Return right

# Time complexity : O(logN).
# Space complexity : O(1).