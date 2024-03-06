# Approach: Neetcode : https://youtu.be/DEJAZBq0FDA
# OR
# Approach 1: Two indexes approach
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                
        return l
    
    
# OR - changing conditions 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums) - 1):
            if nums[j] != nums[j+1]:
                nums[i] = nums[j]
                i += 1
        nums[i] = nums[-1]
        return i + 1
    

# OR - changing conditions 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i

# OR

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex


nums = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))


# Complexity Analysis:
# Let N be the size of the input array.
# Time Complexity: O(N), since we only have 2 pointers, and both the pointers will traverse the array at most 
# once.
# Space Complexity: O(N), since we are not using any extra space.