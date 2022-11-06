# Approach : Brute Force
# Pop out all the duplicates


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) -1 , 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                

nums = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(N^2), for loop with pop method.
# Space Complexity: O(1).