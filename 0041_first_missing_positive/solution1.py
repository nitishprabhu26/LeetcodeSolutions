# Using extra O(n) space and O(n) solution

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = max(nums)
        num_set = set(nums)
        for i in range(1, N + 2):
            if i not in num_set:
                return i
        return 1
            

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(N)


# AND also O(n.logn) solution - using sort and no extra space

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res


nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
obj = Solution()
print(obj.firstMissingPositive(nums))


# Complexity Analysis:
# Time Complexity: O(n.logn), where N is the length of nums.
# Space Complexity: O(1)