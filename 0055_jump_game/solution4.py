# Approach 4: Greedy
# OR 
# Neetcode: https://youtu.be/Yan0cv2cLy8


from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastPos = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
            
        return lastPos == 0


        
nums = [2,3,1,1,4]
obj = Solution()
print(obj.canJump(nums))


# Complexity Analysis
# Time complexity : O(n). We are doing a single pass through the nums array, hence n steps, where n is the length 
# of array nums.
# Space complexity : O(1). We are not using any extra memory.