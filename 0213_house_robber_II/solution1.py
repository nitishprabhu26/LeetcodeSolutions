# Approach 1: Dynamic Programming
# https://leetcode.com/problems/house-robber-ii/solution/
# OR
# Neetcode:
# https://youtu.be/rWAJCfYYOvM


# Intuition:
# Assume we have nums of [7,4,1,9,3,8,6,5] as shown in the figure. Since the start house and last house are 
# adjacent to each other, if the thief decides to rob the start house 7, they cannot rob the last house 5. 
# Similarly, if they select last house 5, they have to start from a house with value 4. Therefore, the final 
# solution that we are looking for is to take the maximum value the thief can rob between houses of list 
# [7,4,1,9,3,8,6] and [4,1,9,3,8,6,5]. For each of the lists, all we need to do is to figure the maximum value 
# the thief can get using the approach in the original House Robber Problem.


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2

# OR

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2


nums = [2,3,2]
obj = Solution()
print(obj.rob(nums))


# Complexity Analysis:
# Time Complexity: O(N) where N is the size of nums. We are accumulating results as we are scanning nums.
# Space Complexity: O(1) since we are not consuming additional space other than 3 additional variables.