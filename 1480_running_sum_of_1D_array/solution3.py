# Approach 2: Using Input Array for Output

# Intuition:
# In the previous approach we created an extra array to store our results. However, we do not actually need to do 
# so. We can obtain the same result without using extra space by performing the same operations on the input array 
# instead.

# Algorithm:
# Increase nums[i] by the previous index's running sum. The previous index's running sum is stored at index i-1 in 
# the input array. We repeat step 1 for all indices from 1 to n-1.


from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return nums


nums = [2, 6, 11, 15]
obj = Solution()
print(obj.runningSum(nums))


# Complexity Analysis:
# Time complexity: O(n) where n is the length of the input array.
# Space complexity: O(1) since we don't use any additional space to find the running sum.