# Approach : Brute Force [Time Limit Exceeded]
# Trying every single subarray
# (Mentioned in https://youtu.be/OKcrLfR-8mE?t=110)


from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 2, len(nums) + 1):
                total = sum(nums[i : j])
                if total % k == 0:
                    return True
        return False


nums = [23,2,4,6,7]
k = 6
obj = Solution()
print(obj.checkSubarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(N^3), where n is the length of the nums.
# Space complexity : O(1). We only need constant spaces to store total variable.
