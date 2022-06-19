# Approach 2: Two Pass

# Intuition and Algorithm:
# Write all the even elements first, then write all the odd elements.


from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return ([x for x in nums if x % 2 == 0] +
                [x for x in nums if x % 2 == 1])
        

nums = [3,1,2,4]
obj = Solution()
print(obj.sortArrayByParity(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(N), the space used by the answer.
