# Using Python Dictionary

from typing import List
     

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                
        for key, val in dict.items():
            if val == 1:
                return key

# OR

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                if dict[num] == 2:
                    del dict[num]
                else:
                    dict[num] += 1
                    
        return dict.popitem()[0]


nums = [2,2,3,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(N), to store dictionary values.