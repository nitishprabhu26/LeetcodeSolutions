# Approach #1 (Space Sub-Optimal) [Accepted]

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        numZeros = 0
        for i in range(len(nums)):
            numZeros += (nums[i]==0)
        
        extraArray = []
        for i in range(len(nums)):
            if nums[i]!=0:
                extraArray.append(nums[i])
                
        while numZeros>0:
            extraArray.append(0)
            numZeros-=1
            
        nums[:] = extraArray
        return nums

nums = [ 0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))

# Complexity Analysis:
# Space Complexity : O(n). Since we are creating the "extraArray" array to store results.
# Time Complexity: O(n).