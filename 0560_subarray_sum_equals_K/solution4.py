# Approach 4: Using Hashmap
# https://youtu.be/fFVZt-6sgyo

# Algorithm:
# We make use of a hashmap map which is used to store the cumulative sum up to all the indices possible along with 
# the number of times the same sum occurs. We store the data in the form: (sum_i, no. of occurrences of sum_i). 
# We traverse over the array nums and keep on finding the cumulative sum. Every time we encounter a new sum, we 
# make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count 
# corresponding to that sum in the hashmap. 
# Further, for every sum encountered, we also determine the number of times the sum 'sum−k' has occurred already, 
# since it will determine the number of times a subarray with sum 'k' has occurred up to the current index. We 
# increment the count by the same amount. 
# After the complete array has been traversed, the count gives the required result.


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        # basecase: having a single prefixsum having subarray sum as 0 (for empty subarray)
        prefixSums = { 0 : 1 }
        
        for n in nums:
            curSum += n
            diff = curSum - k
            # we look for the diff in prefixSum, to find a potential result
            # if so then add the count to res 
            # add the count of prefixSums which sum up to diff, to the result
            res += prefixSums.get(diff, 0)
            
            # also add the curSum to prefixSums hashmap
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res

        
nums = [1,2,3]
k = 3
obj = Solution()
print(obj.subarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(n). The entire nums array is traversed only once.
# Space complexity : O(n). Hashmap map can contain up to n distinct entries in the worst case.