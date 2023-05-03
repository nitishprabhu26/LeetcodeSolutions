# Approach 2 (Sorting) [Accepted]
# Intuition:
# If there are any duplicate integers, they will be consecutive after sorting.


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


# nums = [1,2,3,1]
nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))


# Complexity analysis:
# Time complexity : O(n. logn). For sort function
# Space complexity : O(1). We only used constant extra space.