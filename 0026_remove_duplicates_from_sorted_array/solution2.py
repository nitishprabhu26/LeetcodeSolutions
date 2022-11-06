# Approach : Extra memory - Using set


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        i = 0
        for num in nums_set:
            nums[i] = num
            i += 1
            
        return i
                

nums = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(N). Extra memory used.