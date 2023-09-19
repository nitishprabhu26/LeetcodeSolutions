# Approach 1: Binary Search (modified version)
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/

# In this modified version of binary search algorithm, we are looking for INFLECTION point. 
# eg: 4 5 6 7 2 3
# Inflection point -> (7, 2)
# All the elements to the left of inflection point > first element of the array.
# All the elements to the right of inflection point < first element of the array.

# Algorithm

# 1. Find the mid element of the array.
# 2. If mid element > first element of array this means that we need to look for the inflection point on the 
#    right of mid.
# 3. If mid element < first element of array this that we need to look for the inflection point on the left of 
#    mid.
# 4. We stop our search when we find the inflection point, when either of the two conditions is satisfied:
#       nums[mid] > nums[mid + 1] Hence, mid + 1 is the smallest.
#       nums[mid - 1] > nums[mid] Hence, mid is the smallest.


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            # Also mid-1 can give index out of bound error if the array is [1, 3] (only 2 elements left)
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than 
            # nums[0] or nums[left]
            # if nums[mid] > nums[left]:
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the 
            # left
            else:
                right = mid - 1


nums = [3,4,5,1,2]
obj = Solution()
print(obj.findMin(nums))


# Complexity Analysis:
# Time Complexity : Same as Binary Search O(logN)
# Space Complexity : O(1)