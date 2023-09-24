# Approach 2: One-pass Binary Search
# Neetcode:
# https://youtu.be/U8XENwh8Oy8

# Instead of going through the input array in two passes, we could achieve the goal in one pass with an revised
# binary search. The idea is that we add some additional condition checks in the normal binary search in order
# to better narrow down the scope of the search.

# Algorithm
# As in the normal binary search, we keep two pointers (i.e. start and end) to track the search scope. At each
# iteration, we reduce the search scope into half, by moving either the start or end pointer to the middle
# (i.e. mid) of the previous search scope.

# Here are the detailed breakdowns of the algorithm:

# - Initiate the pointer start to 0, and the pointer end to n - 1.
# - Perform standard binary search. While start <= end:
#   - Take an index in the middle mid as a pivot.
#   - If nums[mid] == target, the job is done, return mid.

#   - Now there could be two situations:

    #   - Pivot element is larger than the first element in the array, i.e. the subarray from the first element
    #     to the pivot is non-rotated.
        #   - If the target is located in the non-rotated subarray:
        #       go left: `end = mid - 1`.
        #   - Otherwise: go right: `start = mid + 1`.

    #   - Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere
    #     between 0 and mid. It implies that the sub-array from the pivot element to the last one is non-rotated
        #   - If the target is located in the non-rotated subarray:
        #       go right: `start = mid + 1`.
        #   - Otherwise: go left: `end = mid - 1`.

# We're here because the target is not found. Return -1.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            # left sorted portion
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right sorted portion
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


# OR
# Neetcode:
# https://youtu.be/U8XENwh8Oy8

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Time complexity : O(log N).
# Space complexity : O(1).