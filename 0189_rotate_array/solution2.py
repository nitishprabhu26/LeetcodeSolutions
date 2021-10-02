# Approach 2: Using Extra Array

# Algorithm:
# We use an extra array in which we place every element of the array at its correct position i.e. the number at index i in the 
# original array is placed at the index (i + k) % length of array. Then, we copy the new array to the original one.

class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 6
obj = Solution()
print(obj.rotate(nums, k))

# Complexity Analysis:
# Time complexity: O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
# Space complexity: O(n). Another array of the same size is used.
