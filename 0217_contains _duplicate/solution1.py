# Approach 1 (Naive Linear Search) [Time Limit Exceeded]


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# OR
# using index function
# https://www.geeksforgeeks.org/python-handling-no-element-found-in-index/ (not needed for this problem)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i,x in enumerate(nums):
            if nums.index(x) != i:
                return True
        return False
    

nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))


# Complexity analysis:
# Time complexity : O(n^2). In the worst case, there are n.(n+1)/2 pairs of integers to check. 
# Space complexity : O(1). We only used constant extra space.