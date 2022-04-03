# Approach: Neetcode
# https://youtu.be/8g78yfzMlao

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # neutralize negative values to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        # marking if a value exists in a input array or not, by overwriting input nums
        # but only for inbound values
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # case where nums[val - 1] == 0, we use a value which is greater than len(nums)
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
                    
        # return the 1st element which has positive value, meaning 'i' is the firstMissingPositive 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
        
            
nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
obj = Solution()
print(obj.firstMissingPositive(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(1)