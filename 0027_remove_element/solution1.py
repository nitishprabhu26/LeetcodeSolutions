# Approach : Brute Force
# Pop out all the matching values


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            else:
                k += 1
        return k
    
# OR

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
        return k              


nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))


# Complexity Analysis:
# Time Complexity: O(N^2), for loop with pop method.
# Space Complexity: O(1).