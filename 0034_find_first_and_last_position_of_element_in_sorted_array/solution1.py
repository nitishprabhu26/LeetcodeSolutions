# Approach: Without Binary search


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexArray=[]
        if len(nums)==0:
            return [-1,-1]
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    indexArray.append(i)
        return [indexArray[0],indexArray[-1]] if len(indexArray)>0 else [-1,-1]


# OR

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        low = nums.index(target)
        if low == -1:
            return [-1, -1]
        
        high = low
        for i in range(low + 1, len(nums)):
            if nums[i] == target:
                high += 1
        
        return [low, high]


# OR

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==0:
            return [-1,-1]
    
        found =[]
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    found.append(i)
                    
            if len(found) == 1:
                return [found[0],found[0]]
            
            return [found[0],found[len(found)-1]]
        
        else:
            return [-1,-1]


# OR

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        left_idx = -1
        right_idx = -1
    
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
                
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                right_idx = i
                break
                
        return [left_idx, right_idx]


nums = [5,7,7,8,8,10]
target = 8
obj = Solution()
print(obj.searchRange(nums, target))


# Complexity Analysis:
# Time complexity : O(n). 
# Space complexity : O(n) or O(1).

