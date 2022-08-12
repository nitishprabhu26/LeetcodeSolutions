# Linear Approach:[Passed]
# Not recomended O(n)


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res_index = 0
        for i in range(len(nums)):
            if nums[i] < target:
                res_index = i + 1
            else:
                break
        
        return res_index

# OR

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])


nums = [1, 3, 5, 6]
target = 5
obj = Solution()
print(obj.searchInsert(nums, target))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1) since it's a constant space solution.