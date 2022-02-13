# Approach 4: Greedy
# OR 
# Neetcode: https://youtu.be/Yan0cv2cLy8

# Once we have our code in the bottom-up state, we can make one final, important observation. From a given 
# position, when we try to see if we can jump to a GOOD position, we only ever use one - the first one (see the 
# break statement). In other words, the left-most one. If we keep track of this left-most GOOD position as a 
# separate variable, we can avoid searching for it in the array. Not only that, but we can stop using the array 
# altogether.

# Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index 
# (currPosition + nums[currPosition] >= leftmostGoodIndex). If we can reach a GOOD index, then our position is 
# itself GOOD. Also, this new GOOD position will be the new leftmost GOOD index. Iteration continues until the 
# beginning of the array. If first position is a GOOD index then we can reach the last index from the first 
# position.

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