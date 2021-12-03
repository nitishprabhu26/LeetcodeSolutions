# Approach 1 (Naive Linear Search) [Time Limit Exceeded]
# - Look for duplicate element in the next k elements.
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1,len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False

nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
obj = Solution()
print(obj.containsNearbyDuplicate(nums,k))

# Complexity analysis:
# Time complexity : Time complexity : O(n.min(k,n)). It costs O(min(k,n)) time for each linear search. Apparently we do at most 
# n comparisons in one search even if k can be larger than n.
# Space complexity : O(1). We only used constant extra space.