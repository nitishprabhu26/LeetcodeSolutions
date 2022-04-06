from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listIndices=[]
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    listIndices.append(i)
                    listIndices.append(j)
                    return listIndices

nums = [2, 6, 11, 15]
target = 8
obj = Solution()
print(obj.twoSum(nums, target))