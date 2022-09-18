# Approach 1: Two Pointers
# https://leetcode.com/problems/3sum/solution/

# We will follow the same two pointers pattern as in Two Sum II. It requires the array to be sorted, so we'll 
# do that first. As our BCR is {O}(n^2), sorting the array would not change the overall time complexity.
# To make sure the result contains unique triplets, we need to skip duplicate values. It is easy to do because 
# repeating values are next to each other in a sorted array.

# Algorithm:
# The implementation is straightforward - we just need to modify twoSumII to produce triplets and skip repeating 
# values.
# 1.For the main function:
#   - Sort the input array nums.
#   - Iterate through the array:
#       - If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
#       - If the current value is the same as the one before, skip it.
#       - Otherwise, call twoSumII for the current position i.
# 2.For twoSumII function:
#   - Set the low pointer lo to i + 1, and high pointer hi to the last index.
#   - While low pointer is smaller than high:
#       - If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
#       - If sum is greater than zero, decrement hi.
#       - Otherwise, we found a triplet:
#           - Add it to the result res.
#           - Decrement hi and increment lo.
#           - Increment lo while the next value is the same as before to avoid duplicates in the result.
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
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                # below line is optional, will get solved in the next loop. 
                # consider eg: [-2,-2,0,2,2] and lo,hi at indices 0 and 4
                # update any one pointer, above 'if' conditions will take care of the other
                # hi -= 1
                lo += 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1


# OR
# Neetcode: https://youtu.be/jzZsG8n2R9A

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while (l < r):
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # update any one pointer, above 'if' conditions will take care of the other
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


inp_nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum(inp_nums))


# Complexity Analysis:
# Time Complexity: O(n^2). twoSumII is O(n), and we call it n times. Sorting the array takes O(nlogn), so overall 
# complexity is O(nlogn + n^2). This is asymptotically equivalent to O(n^2).
# Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. For the 
# purpose of complexity analysis, we ignore the memory required for the output.

