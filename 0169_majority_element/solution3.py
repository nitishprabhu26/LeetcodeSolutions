# Approach 3: Sorting

# Intuition:
# If the elements are sorted in monotonically increasing (or decreasing) order, the majority element can be found 
# at index [n/2] or ( [n/2]+1, incidentally, if n is even).


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]



nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))


# Complexity Analysis:
# Time Complexity: O(n.log n). Sorting array.
# Space Complexity: O(1) or O(n). We sorted nums in place here - if that is not allowed, then we must spend linear 
# additional space on a copy of nums and sort the copy instead.