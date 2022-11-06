# Approach: Sorting + Linear Traversal
# https://youtu.be/cOFAmaMBVps?t=87

# Boundary condition 1 :
# - If single element is at the begining of the list (1st element)
#   eg: [2, 4, 4, 4, 5, 5, 5]
# Boundary condition 2 :
# - If single element is at the end of the list (last element)
#   eg: [4, 4, 4, 5, 5, 5, 6]
# OR 
# - General case: The single element could be inbetween any two clusters
#   eg: [2, 2, 2, 3, 3, 3, 4, 5, 5, 5]


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if nums has only one element, then return that element
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        
        # Boundary cases
        # case1: If single element is at the begining of the list (1st element)
        # if 1st element doesnt have cluster of size 3
        if nums[0] != nums[1]:
            return nums[0]
        
        # if last element doesnt have cluster of size 3
        # case2: If single element is at the end of the list (last element)
        if nums[-1] != nums[-2]:
            return nums[-1]

        # General case: The single element could be inbetween any two clusters
        # initialize index to 1st element
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
            i += 3
            
nums = [2,2,3,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(N + N logN) to iterate over the input array, and for sorting.
# Space complexity : O(N) if we consider space to store the sorted input, else O(1).