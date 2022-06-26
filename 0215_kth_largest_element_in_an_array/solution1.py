# Approach 0: Sort
# The naive solution would be to sort an array first and then return kth element from the end, something like 
# sorted(nums)[-k] on Python. That would be an algorithm of O(N.logN) time complexity and O(1) space complexity. 
# This time complexity is not really exciting so let's check how to improve it by using some additional space.


from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
        # or
        nums.sort()
        return nums[-k]


nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))