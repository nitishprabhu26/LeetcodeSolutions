# Approach: Brute force approach


from typing import List

class Solution:
    def isGood(self, arr, k):
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1
        return 1 if count >= k else 0
        
    def countGood(self, nums: List[int], k: int) -> int:
        good_sub_count = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sub_arr = nums[i : j + 1]
                good_sub_count += self.isGood(sub_arr, k)
        return good_sub_count


nums = [3,1,4,3,2,2,4]
k = 2
obj = Solution()
print(obj.countGood(nums, k))


# Complexity Analysis:
# Time complexity : O(N^4).
# Space complexity : O(1).