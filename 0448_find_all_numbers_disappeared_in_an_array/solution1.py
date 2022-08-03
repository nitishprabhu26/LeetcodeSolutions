# Approach : Brute Force [Time Limit Exceeded]
# Using array: O(n^2)


from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
        return res


nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))


# Complexity Analysis:
# Time Complexity: O(n^2).
# Space Complexity: O(1). No extra space required, other than the space for the output list.