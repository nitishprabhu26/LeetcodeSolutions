# Approach 1: Brute Force

# Intuition:
# We can exhaust the search space in quadratic time by checking whether each element is the majority element.

# Algorithm:
# The brute force algorithm iterates over the array, and then iterates again for each number to count its 
# occurrences. As soon as a number is found to have appeared more than any other can possibly have appeared, 
# return it.


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        
        for num in nums:
            count = 0
            for elem in nums:
                if elem == num:
                    count += 1
            if count > majority_count:
                return num

# OR

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            # count = sum([1 for elem in nums if elem == num])
            # OR
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num



nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))


# Complexity Analysis:
# Time Complexity: O(n^2). The brute force algorithm contains two nested for loops that each run for n iterations, 
# adding up to quadratic time complexity.
# Space Complexity: O(1). The brute force solution does not allocate additional space proportional to the input 
# size.