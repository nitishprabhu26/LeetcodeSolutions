# Approach 1: Binary Search
# OR
# Neetcode: https://youtu.be/s4DPM8ct1pI


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            # If target is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1
            # If target is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1
            # means target is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1


# OR

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # integer overflow handling
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Time complexity: O(logN).
# Space complexity : O(1).
