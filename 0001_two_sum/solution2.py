class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in dict:
                return [dict[y], i]
            else:
                dict[x] = i

# or

# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         dict1 = {}
#         for i in range(0, len(nums)):
#             if target - nums[i] in dict1:
#                 return [dict1[target - nums[i]], i]
#             if nums[i] not in dict1:
#                 dict1[nums[i]] = i

nums = [5,2,2,2,7,5,3,7,4,5,4]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))