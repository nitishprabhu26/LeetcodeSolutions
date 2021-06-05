# https://leetcode.com/problems/3sum/solution/
# Approach 1: Two Pointers
# We will follow the same two pointers pattern as in Two Sum II. It requires the array to be sorted, so we'll do that first.
# As our BCR is {O}(n^2), sorting the array would not change the overall time complexity.
# To make sure the result contains unique triplets, we need to skip duplicate values. It is easy to do because repeating
# values are next to each other in a sorted array.

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i+1, len(nums)-1
        while (lo < hi):
            sum = nums[i]+nums[lo]+nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                # below line is optional, will get solved in the next loop. 
                # consider eg: [-2,-2,0,2,2] and lo,hi at indices 0 and 4
                # hi -= 1
                lo += 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1


inp_nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum(inp_nums))

# Complexity Analysis:

# Time Complexity: O(n^2). twoSumII is O(n), and we call it n times.
# Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2). This is asymptotically equivalent to O(n^2)

# Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. For the purpose 
# of complexity analysis, we ignore the memory required for the output.

