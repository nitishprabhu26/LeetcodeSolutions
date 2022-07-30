# Approach : Neetcode - Binary search
# https://youtu.be/4sQL7R5ySUU


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        
        return [left, right]
        
        
    # leftBias=[True/False], if False then res is rightBiased 
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        
        i = -1
        while l <= r:
            m = (l + r) // 2
            
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
                    
        return i


nums = [5,7,7,8,8,10]
target = 8
obj = Solution()
print(obj.searchRange(nums, target))


# Complexity Analysis:
# Time complexity : O(logN) considering there are N elements in the array. This is because binary search takes 
# logarithmic time to scan an array of N elements. Why? Because at each step we discard half of the array we are 
# scanning and hence, we're done after a logarithmic number of steps. We simply perform binary search twice in 
# this case. 
# Space complexity : O(1) since we only use space for a few variables and our result array, all of which require 
# constant space.