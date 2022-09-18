# Approach 2: Hashset
# https://leetcode.com/problems/3sum/solution/

# We move our pivot element nums[i] and analyze elements to its right. We find all pairs whose sum is equal to
# -nums[i] using the Two Sum: One-pass Hash Table approach, so that the sum of the pivot element (nums[i]) and the 
# pair (-nums[i]) is equal to zero.
# To do that, we process each element nums[j] to the right of the pivot, and check whether a complement 
# -nums[i] - nums[j] is already in the hashset. If it is, we found a triplet. Then, we add nums[j] to the hashset, 
# so it can be used as a complement from that point on.


# Algorithm:
# The main function is the same as in the Two Pointers approach above. Here, we use twoSum (instead of twoSumII), 
# modified to produce triplets and skip repeating values.
# 1.For the main function:
#   - Sort the input array nums.
#   - Iterate through the array:
#       - If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
#       - If the current value is the same as the one before, skip it.
#       - Otherwise, call twoSum for the current position i.
# 2.For twoSum function:
#   - For each index j > i in A:
#       - Compute complement value as -nums[i] - nums[j].
#       - If complement exists in hashset seen:
#           - We found a triplet - add it to the result res.
#           - Increment j while the next value is the same as before to avoid duplicates in the result.
#       - Add nums[j] to hashset seen
# 3.Return the result res.


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
        j = i + 1
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
# Time Complexity: O(n^2). twoSum is O(n), and we call it n times. Sorting the array takes O(nlogn), so overall 
# complexity is O(nlogn + n^2). This is asymptotically equivalent to O(n^2).
# # Space Complexity: O(n) for the hashset.