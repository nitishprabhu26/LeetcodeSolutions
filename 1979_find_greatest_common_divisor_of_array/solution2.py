# Simple approach with iterative GCD


from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        for i in range(min_num, 0, -1):
            if max_num % i == 0 and min_num % i == 0:
                return i


nums = [2,5,6,9,10]
obj = Solution()
print(obj.findGCD(nums))


# Time Complexity : O(min(a,b).
# Auxiliary Space : O(1).