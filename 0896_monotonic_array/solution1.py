# Approach 1: Two Pass

# Intuition:
# An array is monotonic if it is monotone increasing, or monotone decreasing. Since a <= b and b <= c implies 
# a <= c, we only need to check adjacent elements to determine if the array is monotone increasing (or decreasing, 
# respectively). We can check each of these properties in one pass.

# Algorithm:
# To check whether an array A is monotone increasing, we'll check A[i] <= A[i+1] for all i. The check for monotone 
# decreasing is similar.

# https://www.w3schools.com/python/ref_func_all.asp
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) 
                or all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)))
            

nums = [1,2,2,3]
nums = [6,5,4,4]
obj = Solution()
print(obj.isMonotonic(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(1)