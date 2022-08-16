# Approach 1: Brute Force [Time Limit Exceeded]

# Algorithm:
# The simplest method is to consider every possible subarray of the given nums array, find the sum of the 
# elements of each of those subarrays and check for the equality of the sum obtained with the given k. Whenever 
# the sum equals k, we can increment the count used to store the required result.


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i : j + 1]) == k:
                    count += 1
        return count


# OR
# using for loop instead of sum() method

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = 0
                for ele in range(i, j + 1):
                    total += nums[ele]
                if total == k:
                    count += 1
        return count


nums = [1,2,3]
k = 3
obj = Solution()
print(obj.subarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(n^3). Considering every possible subarray takes O(n^2) time. For each of the subarray we 
# calculate the sum taking O(n) time in the worst case, taking a total of O(n^3) time.
# Space complexity : O(n). Constant space is used.
