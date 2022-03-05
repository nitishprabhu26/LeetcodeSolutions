# Approach : Adding upper and lower to nums, beforehand
# https://leetcode.com/problems/missing-ranges/discuss/50631/Ten-line-python-solution/292469

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        res = []
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        return res


nums = [0,1,3,50,75]
lower = 0
upper = 99
obj = Solution()
print(obj.findMissingRanges(nums, lower, upper))


# Complexity Analysis:

# Time Complexity : O(N). This is because we are only iterating over the array once, and at each step, we're 
# performing O(1) operations.

# Space Complexity : O(1)
# The output list has a worst case size of O(N). This case occurs when we have a missing range between each of 
# the consecutive elements in the input array (for example, if the input array contains all even numbers between 
# lower and upper). Apart from this, we aren't using any other additional space, beyond fixed-sized constants 
# that don't grow with the size of the input.

# Extra:
# What would be the space complexity for this? Is it O(N) since we modify nums?
# - Even if the input scales, we will always be inserting 1 item to start of nums and 1 item to the end. 
#   So O(2n) i.e. O(n) (considering input had only 1 element initially)

# However, output space that is simply used to return the output (and not to do any processing) is not counted 
# for the purpose of space complexity analysis. For this reason, the overall space complexity is O(1).