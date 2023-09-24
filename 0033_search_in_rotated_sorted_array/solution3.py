# Approach 1: Find Pivot Index + Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/editorial/

# Overview:
# Define the pivot index as representing the smallest element in nums.
# In a rotated sorted array, the pivot value signifies where the rotation occurs. It partitions the array 
# (of length n) into two sorted portions nums[0 ~ pivot - 1] and nums[pivot ~ n - 1].


# Intuition:
# To pinpoint the pivot value, we can employ a modified binary search algorithm and find the leftmost element 
# that is smaller than or equal to the last element in nums.

# After identifying the middle element in the searching space [left ~ right], we compare nums[mid] with nums[-1].
# - If nums[mid] > nums[-1], it suggests that the pivot value lies on the right of nums[mid]. We will then 
#   proceed with the right half of the search space, which is [mid + 1 ~ right].
# - Otherwise, the pivot value is nums[mid] or it's situated to the left of nums[mid], we continue with the 
#   left half of the searching space, which is [left ~ mid - 1].

# By determining the pivot value, we set the boundaries for our subsequent binary searches. Once we have the 
# pivot value, we can execute two binary searches on each half of the array to locate the target element.


# Algorithm:
# 1.Perform a binary search to locate the pivot element by initializing the boundaries of the searching space 
#   as left = 0 and right = n - 1. While left < right:
#   -   Let mid = left + (right - left) // 2.
#   -   If nums[mid] > nums[n - 1], this suggests that pivot is located to the right of mid, hence we set 
#       left = mid + 1. Otherwise, pivot could be either at mid or to the left of mid, in which case we should 
#       set right = mid - 1.
# 2.Upon completion of the binary search, we have the pivot index denoted as pivot = left.
# 3.nums consists of two sorted subarrays, nums[0 ~ left - 1] and nums[left ~ n - 1].
# 4.Perform a binary search over nums[0 ~ left - 1] for target. If target is within this subarray, return its 
#   index.
# 5.Otherwise, perform a binary search over nums[left ~ n - 1] for target. If target is within this subarray, 
#   return its index. Otherwise, return -1.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer 
        
        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)


nums = [4,5,6,7,0,1,2] 
target = 0
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Let n be the length of nums.
# Time complexity: O(logn)
# - The algorithm requires one binary search to locate pivot, and at most 2 binary searches to find target. 
#   Each binary search takes O(logn) time.
# Space complexity: O(1)
# - We only need to update several parameters left, right and mid, which takes O(1) space.