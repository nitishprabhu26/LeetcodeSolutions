# Approach 3: Binary Search

# Instead of moving two pointers towards the target, we can iterate through each element nums[i], and binary-search
# for a complement value k - nums[i]. This approach is less efficient than the two pointers one, however, it can 
# be more intuitive to come up with.
# Note that the binary search returns the "insertion point" for the searched value, i.e. the position where that 
# value would be inserted to keep the array sorted. So, the binary search result points to the first element that 
# is equal or greater than the complement value. Since our sum must be smaller than k, we consider the element 
# immediately before the found element.

# Algorithm:
# 1. Sort the array.
# 2. For each index i in nums:
#       Binary search for k - nums[i] starting from i + 1.
#       Set j to the position before the found element.
#       If j is less than i:
#           Track maximum nums[i] + nums[j] in the result answer.
# 3. Return the result answer.


# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
from bisect import bisect_left
from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        nums.sort()
        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i + 1) - 1
            if j > i:
                answer = max(answer, nums[i] + nums[j])
        return answer


nums = [34,23,1,24,75,33,54,8]
k = 60
obj = Solution()
print(obj.twoSumLessThanK(nums, k))


# Complexity analysis:
# Time Complexity: O(nlogn) to sort the array and do the binary search for each element.
# Bisect method works on the concept of binary search -> O(log(n))
# Space Complexity: O(1).
