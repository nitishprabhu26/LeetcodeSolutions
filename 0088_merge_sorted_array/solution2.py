# Using sorted method:

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = sorted(nums1[:m] + nums2)
        print(nums1)
        # OR
        # nums1[:m+n] = sorted(nums1[:m] + nums2)
        # OR
        # nums1[:] = sorted(nums1[:m] + nums2)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)