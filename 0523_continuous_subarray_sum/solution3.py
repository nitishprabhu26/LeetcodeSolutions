# Hash map approach
# https://youtu.be/2K92SzwNaPg (preferred) OR https://leetcode.com/problems/continuous-subarray-sum/solution/


from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        # for a special case when reminder of the sum of entire array is '0'
        # so we append (0, 0) to the hashmap
        # eg: nums = [23, 2, 6, 4] and k = 7
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            # if the subarray size is at least two
            elif hash_map[s % k] < i:
                return True
        return False


# OR
# Neetcode: https://youtu.be/OKcrLfR-8mE

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            # if the remainder 'r' occurs for the first time
            if r not in remainder:
                remainder[r] = i
            # if the subarray size is at least two
            elif i - remainder[r] > 1:
                return True
        return False


nums = [23,2,4,6,7]
k = 6
obj = Solution()
print(obj.checkSubarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(nums.length).
# We perform O(nums.length) operations with a hash map, each taking O(1) time on average.
# Space complexity : O(min{nums.length,k}).
# The size of a hash map does not exceed nums.length+1. It also does not exceed kk because there are only k 
# possible remainders.
