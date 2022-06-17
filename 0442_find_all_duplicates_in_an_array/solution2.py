# Approach 2: Sort and Compare Adjacent Elements

# Intuition:
# After sorting a list of elements, all elements of equivalent value get placed together. Thus, when you sort an 
# array, equivalent elements form contiguous blocks.

# Algorithm:
# Sort the array.
# Compare every element with it's neighbors. If an element occurs more than once, it'll be equal to at-least one 
# of it's neighbors.


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ans.append(nums[i])
                i += 1
                    
        return ans


nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(nlogn)+ O(n) ≃ O(nlogn).
# - A performant comparison-based sorting algorithm will run in O(nlogn) time.
# - Traversing the array after sorting takes linear time i.e. O(n).
# Space Complexity: No extra space required, other than the space for the output list. Sorting can be done 
# in-place.

