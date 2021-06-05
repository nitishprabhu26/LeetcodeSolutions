# Approach 2: Hashset

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        seen = set()
        j = i+1
        while (j < len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

inp_nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(inp_nums))

# Complexiety analysis:

# Time Complexity: O(n^2). twoSum is O(n), and we call it n times.

# Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2). This is asymptotically equivalent 
# to O(n^2)
# Space Complexity: O(n) for the hashset.