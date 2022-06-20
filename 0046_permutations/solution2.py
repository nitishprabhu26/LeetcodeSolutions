# Approach : Neetcode.
# https://youtu.be/s7AvT7cGdSo


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result
        

nums = [1,2,3]
obj = Solution()
print(obj.permute(nums))