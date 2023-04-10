# Approach: Two pointers
# https://youtu.be/7hcex-9AkHA


from typing import List

class Solution:        
    def countGood(self, nums: List[int], k: int) -> int:
        hash_map = {}
        pairs = 0
        ans = 0
        # left pointer
        l = 0
        
        for i in range(len(nums)):
            # add every element to hash_map, and keep the count of each element
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
            
            # use the freq of new element to calculate pairs
            pairs += hash_map[nums[i]] - 1
            
            # at any point when pairs is equal or greater than k, 
            # start removing elements from left
            if pairs >= k:
                while l <= i and pairs >= k:
                    # add the remaining elements of the array which are to 
                    # right of right pointer, to the answer 
                    ans += len(nums) - i
                    hash_map[nums[l]] -= 1
                    pairs -= hash_map[nums[l]]
                    if hash_map[nums[l]] == 0:
                        del hash_map[nums[l]]
                    l += 1
        
        return ans


nums = [3,1,4,3,2,2,4]
k = 2
obj = Solution()
print(obj.countGood(nums, k))


# Complexity Analysis:
# Time complexity : O(2.n). Two pointers can go over all the elements of the input array.
# Space complexity : O(1).