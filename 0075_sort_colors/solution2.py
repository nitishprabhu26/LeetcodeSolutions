# Approach: Neetcode (Bucket sort and Quicksort Partition)
# https://youtu.be/4xbWSRZHqac

# Bucket sort:

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # O(n) time and O(1) memory i.e. O(3) for the buxket array
        bucket = [0] * 3
        for i in nums:
            bucket[i] += 1
            
        j = 0
        for i in range(len(bucket)):
            while bucket[i] > 0:
                nums[j] = i
                j += 1
                bucket[i] -= 1
        return nums


# AND
# Quicksort Partition:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        return nums


nums = [2,0,2,1,1,0]
obj = Solution()
print(obj.sortColors(nums))


# Complexity Analysis:
# Time complexity : O(N) since it's one pass along the array of length N.
# Space complexity : O(1) since it's a constant space solution.