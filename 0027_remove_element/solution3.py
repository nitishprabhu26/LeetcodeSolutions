# Approach 2: Two Pointers - when elements to remove are rare

# Intuition
# Now consider cases where the array contains few elements to remove. 
# For example, nums = [1,2,3,5,4], val = 4. The previous algorithm will do unnecessary copy operation of the first 
# four elements. 
# Another example is nums = [4,1,2,3,5], val = 4. It seems unnecessary to move elements [1,2,3,5] one step left as 
# the problem description mentions that the order of elements could be changed.

# Algorithm:
# When we encounter nums[i] = val, we can swap the current element out with the last element and dispose the last 
# one. This essentially reduces the array's size by 1.
# Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in 
# the next iteration we will still check this element.


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # reduce array size by one
                n -= 1
            else:
                i += 1
                
        return n
                

nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))


# Complexity Analysis:
# Time Complexity: O(n). Both i and n traverse at most n steps. In this approach, the number of assignment 
# operations is equal to the number of elements to remove. So it is more efficient if elements to remove are rare.
# Space Complexity: O(1).