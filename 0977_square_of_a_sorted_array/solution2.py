# Approach 2: Two Pointer
# OR
# Neetcode: https://youtu.be/FPCZsG_AkUg


# Intuition:
# Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order,
# then some non-negative elements with squares in increasing order.
# For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1],
# and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part in 
# reverse, and the positive part in the forward direction.

# Algorithm:
# We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive 
# direction, and another i in the negative direction.
# Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together 
# using a two-pointer technique.


class Solution:
    def sortedSquares(self, nums: int) -> int:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n-1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result


nums = [-4, -1, 0, 3, 10]
obj = Solution()
print(obj.sortedSquares(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N) if you take output into account and O(1) otherwise.
