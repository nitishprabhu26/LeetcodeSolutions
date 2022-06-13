# Approach 2: Recursion with Memoization

# Algorithm:
# In the last approach, we can observe that a lot of redundant function calls were made with the same value of i 
# as the current index and the same value of sum as the current sum, since the same values could be obtained 
# through multiple paths in the recursion tree. In order to remove this redundancy, we make use of memoization as 
# well to store the results which have been calculated earlier.

# Thus, for every call to calculate(nums, i, sum, target), we store the result obtained in memo[i][sum + total], 
# where total stands for the sum of all the elements from the input array. The factor of total has been added as 
# an offset to the sum value to map all the sums possible to positive integer range. 
# eg: if nums = [1,1,1,1,1], then
# we can pass in len(nums) possible values,
# And for sum
# if all '+' added to all indices -> sum = 5
# if all '-' added to all indices -> sum = -5
# so we need (sum * 2) + 1 possible indices to store all possible values, for each i.
# To keep everything in positive range, we add the factor of total as an offset to the sum value.
# By making use of memoization, we can get the result of each redundant function call in constant time.


from typing import List

class Solution:
    total = 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total = sum(nums)
        memo = [ [float('-inf')]*(2 * self.total + 1) for i in range(len(nums))]
        return self.calculate(nums, 0, 0, target, memo)
    
    def calculate(self, nums, i, sum, target, memo):
        if i == len(nums):
            if sum == target:
                return 1
            else:
                return 0
        else:
            if memo[i][sum + self.total] != float('-inf'):
                return memo[i][sum + self.total]
            add = self.calculate(nums, i + 1, sum + nums[i], target, memo)
            subtract = self.calculate(nums, i + 1, sum - nums[i], target, memo)
            memo[i][sum + self.total] = add + subtract
            return memo[i][sum + self.total]
        


nums = [1,1,1,1,1]
target = 3

obj = Solution()
print(obj.findTargetSumWays(nums, target))


# Complexity Analysis
# Time complexity: O(t⋅n). The memo array of size O(t⋅n) has been filled just once. Here, t refers to the sum of 
# the nums array and n refers to the length of the nums array.
# Space complexity: O(t.n). The depth of the recursion tree can go up to n. The memo array contains t.n elements.
