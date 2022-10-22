# Approach 1: Maintain Array Sum

# Intuition and Algorithm:
# Let's try to maintain S, the sum of the array throughout one query operation.
# When acting on an array element nums[index], the rest of the values of nums remain the same. Let's remove 
# nums[index] from S (if it is even), then add nums[index] + val back (if it is even.)

from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S = sum( x for x in nums if x % 2 == 0)
        ans = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                S -= nums[idx]    
            nums[idx] += val

            if nums[idx] % 2 == 0:
                S += nums[idx]
            ans.append(S)
            
        return ans
        

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
obj = Solution()
print(obj.sumEvenAfterQueries(nums, queries))


# Complexity Analysis:
# Time Complexity: O(N + Q), where N is the length of nums and Q is the number of queries.
# Space complexity : O(Q), though we only allocate O(1) additional space.