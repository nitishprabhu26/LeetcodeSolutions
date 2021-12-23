# Approach 1 (Naive Linear Search) [Time Limit Exceeded]

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j)<=k:
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
# Time complexity : O(n^2). In the worst case, there are n(n+1)/2 pairs of integers to check. 
# Space complexity : O(1). We only used constant extra space.