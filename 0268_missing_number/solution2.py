# Approach #1 Sorting [Accepted]

# Algorithm:
# First, we sort nums. Then, we check the two special cases that can be handled in constant time - ensuring that 0 
# is at the beginning and that n is at the end. Given that those assumptions hold, the missing number must 
# somewhere between (but not including) 0 and n.


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))


# Complexity Analysis:
# Time complexity : O(nlgn). 
# The sort invocation (which runs in O(nlgn) time for Python and Java).
# Space complexity : O(1) (or O(n)).
# In the sample code, we sorted nums in place, allowing us to avoid allocating additional space. If modifying 
# nums is forbidden, we can allocate an O(n) size copy and sort that instead.