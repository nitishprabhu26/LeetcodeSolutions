# difference between len of list and set


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        numSet = set()
        for num in nums:
            numSet.add(num)
        numSetLen = len(numSet)
        if numsLen-numSetLen > 0:
            return True
        else:
            return False

# OR
# 1-liner
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False


nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))


# Complexity analysis:
# Time complexity : O(n). 
# Space complexity : O(n). We only used constant extra space.