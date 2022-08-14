# Approach 3: One-pass Hash Table:
# OR
# Neetcode: https://youtu.be/KLlXCFG5TnA

# It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look 
# back to check if current element's complement already exists in the table. If it exists, we have found a 
# solution and return immediately.
 

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in dict:
                return [dict[y], i]
            else:
                dict[x] = i


# OR

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0, len(nums)):
            if target - nums[i] in dict1:
                return [dict1[target - nums[i]], i]
            else:
                dict1[nums[i]] = i


nums = [5,2,2,2,7,5,3,7,4,5,4]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))


# Complexity Analysis:
# Time complexity : O(n). We traverse the list containing n elements only once. Each look up in the table costs 
# only O(1) time.
# Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, 
# which stores at most n elements.