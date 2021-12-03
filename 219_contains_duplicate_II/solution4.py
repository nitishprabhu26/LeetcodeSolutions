# https://youtu.be/UuE6Zk9H6FM
# Using Dictionary by storing value index pair

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, x in enumerate(nums):
            if x in dict and abs(i - dict[x]) <= k:
                return True
            dict[x] = i
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
# Time complexity : Time complexity : O(n). 
# Space complexity : O(n).