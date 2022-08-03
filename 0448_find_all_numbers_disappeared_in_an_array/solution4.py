# Approach : Neetcode
# O(1) Space InPlace Modification Solution : https://youtu.be/8i-f24YFWC4


from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []    
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
                
        return res
        
        
nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(1) since we are reusing the input array itself as a hash table and the space occupied by the 
# output array doesn't count toward the space complexity of the algorithm.