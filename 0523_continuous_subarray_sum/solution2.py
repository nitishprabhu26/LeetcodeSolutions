# Approach : Brute force without using 'sum' keyword [Time Limit Exceeded]
# Using continous sum array to calculate the sum for subarray's (Prefix Sum)
# (Mentioned in https://youtu.be/OKcrLfR-8mE?t=110)


from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_arr = [0] * len(nums)
        cnt_sum = 0
        for i in range(len(nums)):
            cnt_sum += nums[i]
            sum_arr[i] = cnt_sum
            
        # append an extra zero at the begining, for next calculations
        sum_arr = [0] + sum_arr
                
        total = 0
        for i in range(len(nums)):
            for j in range(i + 2, len(nums) + 1):
                total = sum_arr[j] - sum_arr[i]
                if total % k == 0:
                    return True
        return False


nums = [23,2,4,6,7]
k = 6
obj = Solution()
print(obj.checkSubarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(N^2), where n is the length of the nums. We dont use sum method here.
# Space complexity : O(N). To store continous sum array values.
