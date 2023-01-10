# Approach 3: Find Lower bound
# https://leetcode.com/problems/binary-search/solution/

# Algorithm:
# - Initialize the boundaries of the search space as left = 0 and right = nums.size - 1 (Note that the maximum 
#   insert position can be nums.size - 1)
# - If there are elements in the range [left, right], we find the middle index mid = (left + right) / 2 and 
#   compare the middle value nums[mid] with target:
#   -   If nums[mid] >= target, let right = mid and repeat step 2.
#   -   If nums[mid] < target, let left = mid + 1 and repeat step 2.
# - We finish the loop and left stands for the insert position:
#   -   If left < nums.size and nums[left] = target, return left.
# - Otherwise, return -1.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set the left and right boundaries
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1


nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Let n be the size of the input array nums.
# Time complexity: O(logN). nums is divided into half each time. In the worst-case scenario, we need to cut nums 
# until the range has no element, it takes logarithmic time to reach this break condition.
# Space complexity : O(1). During the loop, we only need to record three indexes, left, right, and mid, they take 
# constant space.
