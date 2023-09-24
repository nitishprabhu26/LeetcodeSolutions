# Approach 2: Find Pivot Index + Binary Search with Shift
# https://leetcode.com/problems/search-in-rotated-sorted-array/editorial/

# Intuition:
# The array we're working with has been rotated by a certain number of steps, which means we can't apply a 
# regular binary search to the modified array. However, if we can revert this array to its original sorted form, 
# then a conventional binary search becomes a viable approach.

# Our key task is to locate pivot, the index of the smallest value in nums. Notably, nums[pivot] would have 
# been at index 0 in the unrotated, original array. Hence, if we were to rotate it to the right by n - pivot 
# steps (taking the modulus of n into account), it would return to its original position, index 0.

# Applying the same transformation to every element enables us to revert the rotated array back to its 
# original, sorted form.

# At this point, we can perform a conventional binary search to locate the target. Let's assume that 
# nums[i] = target. Remembering that we had to shift every element to the right by n - pivot steps to reach 
# the sorted version of nums, we now need to shift the index in the sorted nums to the left by n - pivot steps 
# to find its corresponding index, i, in the original nums. This gives us i - (n - pivot) (taking the modulus 
# of n into account).

# Crucially, there's no need to actually create the sorted version of nums from the original nums. We can 
# simply represent the sorted nums by shifting the indices.


# Algorithm:
# 1.Perform a binary search to locate the pivot element by initializing the boundaries of the searching space 
#   as left = 0 and right = n - 1. While left < right:
#   -   Let mid = left + (right - left) // 2.
#   -   If nums[mid] > nums[n - 1], this suggests that pivot is located to the right of mid, hence we set 
#       left = mid + 1. Otherwise, pivot could be either at mid or to the left of mid, in which case we should 
#       set right = mid - 1.
# 2.Upon completion of the binary search, we have the pivot index denoted as pivot = left.
# 3.Set the boundaries of the search space as (pivot + shift) % n and (pivot - 1 + shift) % n.
# 4.While left < right, we get the middle index mid = (left + right) // 2, and compare 
#   nums[(mid - shift + n) % n] with target.
#   -   If nums[(mid - shift + n) % n] is equal to target, return mid - shift + n
#   -   If nums[(mid - shift + n) % n] > target, continue with the left half by setting right as mid - 1.
#   -   If nums[(mid - shift + n) % n] < target, continue with the right half by setting left as mid + 1.
# 5.Return -1 once the binary search is complete.


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
        
        # Shift elements in circular manner, with the pivot element at index 0.
        # Then perform a regular binary search
        def shiftedBinarySearch(pivot_index, target):
            shift = n - pivot_index
            left, right = (pivot_index + shift) % n, (pivot_index - 1 + shift) % n

            while left <= right:
                mid = (left + right) // 2
                if nums[(mid - shift) % n] == target:
                    return (mid - shift) % n
                elif nums[(mid - shift) % n] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
            
        return shiftedBinarySearch(left, target)


nums = [4,5,6,7,0,1,2] 
target = 0
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Let n be the length of nums.
# Time complexity: O(logn)
# - The algorithm requires one binary search to locate pivot, and one binary search over the shifted indices 
#   to find target. Each binary search takes O(logn) time.
# Space complexity: O(1)
# - We only need to update several parameters left, right, mid and shift, which takes O(1) space.