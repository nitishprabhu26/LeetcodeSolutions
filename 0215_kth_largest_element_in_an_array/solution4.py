# Approach 2: Quickselect (Neetcode)
# https://youtu.be/XEmy13g1Qxc


from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k is the index that we are looking for
        k = len(nums) - k
        
        def quickSelect(l, r):
            # we choose rightmost value as the pivot
            pivot, p = nums[r], l
            # up to r, excluding 'r'
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)


nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))


# Complexity analysis:
# Time complexity : O(N) in the average case, O(N^2) in the worst case.
# Space complexity : O(1).