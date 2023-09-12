# Brute force solution: O(n^2) [Time Limit Exceeded]
# Using the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_result = []
        for i in range(len(nums)):
            prod_val = 1
            for j in range(len(nums)):
                if j != i:
                    prod_val *= nums[j]
            prod_result.append(prod_val)
        return prod_result


nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))


# Complexity analysis:
# Time complexity : O(N^2) where N represents the number of elements in the input array. We use two iterations.
# Space complexity : O(1), while ignoring the array to store result.
