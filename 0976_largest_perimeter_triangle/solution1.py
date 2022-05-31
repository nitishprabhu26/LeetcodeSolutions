# Approach 1: Sort

# Intuition
# Without loss of generality, say the sidelengths of the triangle are a ≤ b ≤ c. The necessary and sufficient 
# condition for these lengths to form a triangle of non-zero area is a + b > c.
# Say we knew c already. There is no reason not to choose the largest possible a and b from the array. If 
# a + b > c, then it forms a triangle, otherwise it doesn't.

# Algorithm:
# This leads to a simple algorithm: Sort the array. For any c in the array, we choose the largest possible 
# a ≤ b ≤ c: these are just the two values adjacent to c. If this forms a triangle, we return the answer.


from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# OR

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(2, len(nums)):
            if nums[i] + nums[i-1] > nums[i-2]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
        

nums = [2,1,2]
obj = Solution()
print(obj.largestPerimeter(nums))


# Complexity Analysis:
# Time Complexity: O(NlogN), where N is the length of A.
# Space complexity : O(1).
