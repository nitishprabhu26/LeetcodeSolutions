# Approach 3: Hash Table

# Intuition:
# Keep a sliding window of k elements using Hash Table.

# Algorithm:
# - Loop through the array, for each element do
#   -   Search current element in the HashTable, return true if found
#   -   Put current element in the HashTable
#   -   If the size of the HashTable is larger than k, remove the oldest item.
# - Return false


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i, x in enumerate(nums):
            if x in hashset:
                return True
            hashset.add(x)
            if len(hashset) > k:
                hashset.remove(nums[i-k])
        return False


# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
nums = [1,2,3,1,2,3]
k = 2
obj = Solution()
print(obj.containsNearbyDuplicate(nums,k))


# Complexity analysis:
# Time complexity : O(n). We do n operations of search, delete and insert, each with constant time complexity.
# Space complexity : O(min(n,k)). The extra space required depends on the number of items stored in the hash 
# table, which is the size of the sliding window, min(n,k).