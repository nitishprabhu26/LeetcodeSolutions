# Approach: Greedy

# Intuition:
# The one thing that we should focus on here is the fact that the problem description says non-decreasing, which 
# is just another way of saying increasing. In this case, it means the next element must always be greater than or 
# equal to the current element. Thus, in an array, the item on the left must be less than or equal to the item on 
# the right. Since we can only rectify a single violation of this rule, if more than one violation exists, it is 
# impossible to make the array non-decreasing.

# eg: https://leetcode.com/problems/non-decreasing-array/solution/
# The basic decision making process for fixing a violation is listed below. Without considering the number at the 
# index i - 2, we won't be able to choose between updating nums[i] or nums[i - 1]. The modification has to fit in 
# with the sorted nature of the array.
# if nums[i - 2] > nums[i] then
#     nums[i] = nums[i - 1]
# else
#     nums[i - 1] = nums[i]

# Algorithm:
# 1.We iterate over the array until we reach the end of the array or find a violation.
# 2.If we reach the end of the array, we know it is sorted and we return true.
# 3.Otherwise, we found a violation. We consider the nums[i - 2] to fix the violation.
#   - If the violation is at the index 1, we won't have a nums[i - 2] available. In that case we simply set 
#     nums[i - 1] equal to nums[i].
#   - Otherwise, we check if nums[i - 2] <= nums[i] in which case we set nums[i - 1] equal to nums[i].
#   - Finaly, if nums[i - 2] > nums[i], then we set nums[i] equal to nums[i - 1].
# 4.Once we make the modification, we simply iterate over the remaining array. If we find another violation, we 
#   return false. Otherwise, we return true once the iteration is complete.


from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_violations = 0

        for i in range(1, len(nums)):
            
            if nums[i - 1] > nums[i]:
                
                if num_violations == 1:
                    return False
                
                num_violations += 1
                
                # for the case: 1, 4, 3; the correct modification is to change the number 4 to 3
                # resulting in 1, 3, 3
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                # for the case: 4, 5, 3; the correct modification is to change the number 3 to 5
                # resulting in 4, 5, 5
                else:
                    nums[i] = nums[i - 1]
                    
        return True
        

nums = [4,2,3]
obj = Solution()
print(obj.checkPossibility(nums))


# Complexity Analysis:
# Time Complexity: O(n) considering there are n elements in the array and we process each element at most once.
# Space Complexity: O(1) since we don't use any additional space apart from a couple of variables for executing 
# this algorithm.
