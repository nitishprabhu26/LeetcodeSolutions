# Approach 1: Two Pointers
# OR
# https://youtu.be/Pcd1ii9P9ZI

# Intuition
# We can keep two pointers i and j, where i is the slow-runner while j is the fast-runner.

# Algorithm:
# When nums[j] equals to the given value, skip this element by incrementing j. As long as nums[j] != val, we copy 
# nums[j] to nums[i] and increment both indexes at the same time. Repeat the process until j reaches the end of 
# the array and the new length is i.


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        return i
                

nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))


# Complexity Analysis:
# Time Complexity: O(n), Assume the array has a total of n elements, both i and j traverse at most 2n steps.
# Space Complexity: O(1).