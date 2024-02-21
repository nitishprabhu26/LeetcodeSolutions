# Approach : Neetcode
# https://youtu.be/nIVW4P8b1VA
# Not inflection point approach

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if sliced array is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = ( l + r ) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
        

nums = [3,4,5,1,2]
obj = Solution()
print(obj.findMin(nums))

# Complexity Analysis:
# Time Complexity : Same as Binary Search O(logN)
# Space Complexity : O(1)