# Approach 2: Find Upper bound
# https://leetcode.com/problems/binary-search/solution/

# Intuition:
# Here we introduce an alternative way to implement binary search: instead of looking for target in the array 
# nums, we look for the insert position where we can put target in without disrupting the order.
# Generally, we have two inserting ways, insert into the rightmost possible position which we called finding the 
# upper bound, and insert into the leftmost possible position which we called finding the lower bound. 
# We will implement them in following approaches.
# - If nums[mid] < target, the insert position is on mid's right, so we let left = mid + 1 to discrad the left 
#   half and mid.
# - If nums[mid] = target, the insert position is on mid's right, so we let left = mid + 1 to discrad the left 
#   half and mid.
# - If nums[mid] > target, mid can also be the insert position. So we let right = mid to discard the right half 
#   while keeping mid.
# Therefore, we merged the two conditions nums[mid] = target and nums[mid] < target and there are only two 
# condition in the if-else statement!
# Once the loop stops, left stands for the insert position and left - 1 is the largest element that is no larger 
# than target. We just need to check if nums[left - 1] equals target. 
# Note this boundary condition where left = 0, it means all elements in nums are larger than target, so there is 
# no target in nums.

# Algorithm:
# - Initialize the boundaries of the search space as left = 0 and right = nums.size (Note that the maximum 
#   insert position can be nums.size)
# - If there are elements in the range [left, right], we find the middle index mid = (left + right) / 2 and 
#   compare the middle value nums[mid] with target:
#   -   If nums[mid] <= target, let left = mid + 1 and repeat step 2.
#   -   If nums[mid] > target, let right = mid and repeat step 2.
# - We finish the loop and left stands for the insert position:
#   -   If left > 0 and nums[left - 1] = target, return left - 1.
#   -   Otherwise, return -1.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set the left and right boundaries
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1


nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))


# Complexity Analysis:
# Let n be the size of the input array nums.
# Time complexity: O(log N). nums is divided into half each time. In the worst-case scenario, we need to cut 
# nums until the range has no element, it takes logarithmic time to reach this break condition.
# Space complexity : O(1). During the loop, we only need to record three indexes, left, right, and mid, they 
# take constant space.
