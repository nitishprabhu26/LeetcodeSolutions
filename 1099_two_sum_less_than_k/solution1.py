# Approach 1: Brute Force

# Algorithm:
# 1. For each index i in nums:
#       For each index j > i in nums:
#           If nums[i] + nums[j] is less than k:
#               Track maximum nums[i] + nums[j] in the result answer.
# 2. Return the result answer.


from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < k and sum > maximum:
                    maximum = sum
        return maximum if maximum > 0 else -1

# OR

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < k:
                    answer = max(answer, sum)
        return answer


nums = [34,23,1,24,75,33,54,8]
k = 60
obj = Solution()
print(obj.twoSumLessThanK(nums, k))


# Complexity analysis:
# Time Complexity: O(n^2). We have 2 nested loops.
# Space Complexity: O(1).
