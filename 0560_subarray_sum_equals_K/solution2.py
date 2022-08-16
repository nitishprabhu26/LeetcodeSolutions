# Approach 2: Using Cumulative Sum [Time Limit Exceeded]

# Algorithm:
# Instead of determining the sum of elements every time for every new subarray considered, we can make use of a 
# cumulative sum array, sum. Then, in order to calculate the sum of elements lying between two indices, we can 
# subtract the cumulative sum corresponding to the two indices to obtain the sum directly, instead of iterating 
# over the subarray to obtain the sum.
# In this implementation, we make use of a cumulative sum array, sum, such that sum[i] is used to store the 
# cumulative sum of nums array up to the element corresponding to the (i - 1)^{th} index. Thus, to determine the 
# sum of elements for the subarray nums[i : j], we can directly use sum[j + 1] - sum[i].

# eg: if nums = [1, 2, 3]
#        sum  = [0, 1, 3, 6]
# nums[i : j] = sum[j + 1] - sum[i]
# nums[i : 2] = sum[2 + 1] - sum[1]
#             = sum[3] - sum[1]
#             = 6 - 1
#             = 5


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_arr = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            sum_arr[i] = sum_arr[i - 1] + nums[i - 1]
            
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum_arr[j] - sum_arr[i] == k:
                    count += 1
        
        return count

        
nums = [1,2,3]
k = 3
obj = Solution()
print(obj.subarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(n^2). Considering every possible subarray takes O(n^2) time. Finding out the sum of any 
# subarray takes O(1) time after the initial processing of O(n) for creating the cumulative sum array.
# Space complexity : O(n). Cumulative sum array sum of size n+1 is used.