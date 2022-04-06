# Approach 2: Two-pass Hash Table:

# To improve our run time complexity, we need a more efficient way to check if the complement exists in the 
# array. 
# If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each 
# element in the array to its index? A hash table.

# We reduce the look up time from O(n) to O(1) by trading space for speed. A hash table is built exactly for 
# this purpose, it supports fast look up in near constant time. 

# A simple implementation uses two iterations. In the first iteration, we add each element's value and its 
# index to the table. Then, in the second iteration we check if each element's complement (target−nums[i]) 
# exists in the table. 
# Beware that the complement must not be nums[i] itself!


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]]=i
        for i in range(len(nums)):
            y = target - nums[i]
            if y in dict and dict[y]!=i:
                return [i, dict[y]]

nums = [2, 6, 11, 15]
target = 8
obj = Solution()
print(obj.twoSum(nums, target))


# Complexity Analysis:
# Time complexity : O(n). We traverse the list containing n elements exactly twice. Since the hash table 
# reduces the look up time to O(1), the time complexity is O(n).
# Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, 
# which stores exactly n elements.