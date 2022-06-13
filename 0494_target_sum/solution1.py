# Approach 1: Brute Force [Time Limit Exceeded]

# Algorithm:
# The brute force approach is based on recursion. We need to try to put both the + and - symbols at every location 
# in the given nums array and find out the assignments which lead to the required result target.
# For this, we make use of a recursive function calculate(nums, i, sum, target), which returns the assignments 
# leading to the sum target, starting from the i^{th} index onwards, provided the sum of elements up to the i^{th} 
# element is sum. This function appends a + sign and a - sign both to the element at the current index and calls 
# itself with the updated sum as sum + nums[i] and sum - nums[i] respectively along with the updated current index 
# as i+1. Whenever we reach the end of the array, we compare the sum obtained with target. If they are equal, we 
# increment the count value to be returned.


from typing import List

class Solution:
    count = 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.calculate(nums, 0, 0, target)
        return self.count
    
    def calculate(self, nums, i, sum, target):
        if i == len(nums):
            if sum == target:
                self.count += 1
        else:
            self.calculate(nums, i + 1, sum + nums[i], target)
            self.calculate(nums, i + 1, sum - nums[i], target)


nums = [1,1,1,1,1]
target = 3

obj = Solution()
print(obj.findTargetSumWays(nums, target))


# Complexity Analysis
# Time complexity: O(2^n). Size of recursion tree will be 2^n. n refers to the size of nums array.
# Space complexity: O(n). The depth of the recursion tree can go up to n.
