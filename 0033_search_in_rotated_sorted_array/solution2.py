# Approach 1: Binary search
# The problem is to implement a search in O(logN) time that gives an idea to use a binary search.

# The algorithm is quite straightforward : (check screenshots for eg)
# 1. Find a rotation index rotation_index, i.e. index of the smallest element in the array. Binary search works 
# just perfect here.
# 2. Rotation_index splits array in two parts. Compare nums[0] and target to identify in which part one has to 
# look for target.
# 3. Perform a binary search in the chosen part of the array.


class Solution:
    def search(self, nums, target):
        
        # modified binary search to find the smallest element
        def find_rotate_index(left, right):
            # the array nums is unchanged, rotation index is 0
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)


nums = [4,5,6,7,0,1,2] 
target = 0
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Time complexity : O(log N). 
# Space complexity : O(1).