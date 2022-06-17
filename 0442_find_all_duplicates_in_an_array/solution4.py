# Approach 4: Mark Visited Elements in the Input Array itself

# Intuition:
# All the above approaches have ignored a key piece of information in the problem statement:
# The integers in the input array arr satisfy 1 ≤ arr[i] ≤ n, where n is the size of array.
# This presents us with two key insights:
#   1. All the integers present in the array are positive. i.e. arr[i] > 0 for any valid index i.
#   2. The decrement of any integers present in the array must be an accessible index in the array. i.e. for any 
#      integer x in the array, x-1 is a valid index, and thus, arr[x-1] is a valid reference to an element in the 
#      array.

# Algorithm:
# 1. Iterate over the array and for every element x in the array, negate the value at index abs(x)-1.
#   -   The negation operation effectively marks the value abs(x) as seen / visited.
# 2. Iterate over the array again, for every element x in the array:
#   -   If the value at index abs(x)-1 is positive, it must have been negated twice. Thus abs(x) must have appeared 
#       twice in the array. We add abs(x) to the result.
#   -   In the above case, when we reach the second occurrence of abs(x), we need to avoid fulfilling this 
#       condition again. So, we'll additionally negate the value at index abs(x)-1.


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            nums[abs(num) - 1] *= -1
        
        for num in nums:
            if nums[abs(num) - 1] > 0:
                ans.append(abs(num))
                # to avoid duplicates
                nums[abs(num) - 1] *= -1
                        
        return ans


# OR
# with just one for loop(avoiding first for loop to negate all elements)
# https://youtu.be/aMsSF1Il3IY


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                ans.append(abs(num))
            nums[index] *= -1
                
        return ans



nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(n). We iterate over the array twice. Each negation operation occurs in constant time.
# Space Complexity: No extra space required, other than the space for the output list. We re-use the input array 
# to store visited status.

