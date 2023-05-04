# Approach 1: Brute Force

# Algorithm:
# The brute force approach is simple. Loop through each element x and find if there is another value that equals 
# to target - x.


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# OR

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listIndices = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    listIndices.append(i)
                    listIndices.append(j)
                    return listIndices

                    
nums = [2, 6, 11, 15]
target = 8
obj = Solution()
print(obj.twoSum(nums, target))


# Complexity Analysis:
# Time complexity : O(n^2)
# Space complexity : O(1)
