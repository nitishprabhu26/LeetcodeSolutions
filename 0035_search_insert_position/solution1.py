# Approach 1: Binary Search

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return left


nums = [1, 3, 5, 6]
# target = 9
target = 0
obj = Solution()
print(obj.searchInsert(nums, target))


# Complexity Analysis:
# Time complexity : O(logN).
# Space complexity : O(1) since it's a constant space solution.
