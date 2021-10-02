# Approach 4: Using Reverse
# Algorithm:
# This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array come to the front 
# and the rest of the elements from the front shift backwards.

# In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the 
# rest n−k elements gives us the required result.

# Let n=7 and k=3.
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
            
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 6
obj = Solution()
print(obj.rotate(nums, k))

# Complexity Analysis:
# Time complexity: O(n). n elements are reversed a total of three times.
# Space complexity: O(1). No extra space is used.
