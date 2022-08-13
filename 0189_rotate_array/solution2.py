# Approach 1: Brute Force [Time Limit Exceeded]
# The simplest approach is to rotate all the elements of the array in k steps by rotating the elements by 1 unit 
# in each step.


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # speed up the rotation
        k %= len(nums)
        
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        print(nums)


nums = [1,2,3,4,5,6,7]
k = 6
obj = Solution()
print(obj.rotate(nums, k))


# Complexity Analysis:
# Time complexity: O(n×k). All the numbers are shifted by one step(O(n)), k times.
# Space complexity: O(1). No extra space is used.
