# Doesnt work for one of the long inputs on Leetcode - Time limit exceeded
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i != j and i!=k and k!= j and nums[i]+nums[j]+nums[k] == 0:
                        sorted_array=[nums[i],nums[j],nums[k]]
                        sorted_array.sort()
                        if sorted_array not in res:
                            res.append(sorted_array)
        return res


inp_nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(inp_nums))


# Complexity Analysis:
# Time Complexity: O(n^3). 
# Space Complexity: O(1).