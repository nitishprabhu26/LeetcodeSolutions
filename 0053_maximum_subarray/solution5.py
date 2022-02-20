# Approach 3: Divide and Conquer (Advanced - hard to understand - go with solution3.py)
# https://leetcode.com/problems/maximum-subarray/solution/

# Intuition:
# This approach is slower than the second approach and uses more space, it uses recursion 
# Divide and conquer algorithms involve splitting up the input into smaller chunks until they're small enough to 
# be easily solved, and then combining the solutions to get the final overall solution.

# If we were to split our input in half, then logically the optimal subarray either:
# - Uses elements only from the left side
# - Uses elements only from the right side
# - Uses a combination of elements from both the left and right side

# Thus, the answer is simply the largest of:
# - The maximum subarray contained only in the left side
# - The maximum subarray contained only in the right side
# - The maximum subarray that can use elements from both sides

# Finding the maximum subarray from the left and right half is straightforward - just recurse using the respective 
# half of the array. So, the hard part is figuring out how to find the best subarray that uses elements from both 
# sides. 
# Lets use a smaller example, nums = [5, -2, 1, -3, 4, -2, 1]. 
# Since we want to use elements from both sides, we also must use the middle element, -3. Now, we can also take 
# from the left and the right, but every element must be connected to the middle (since we're still forming a 
# subarray).
# The fact that every element must be connected to the middle actually makes our lives a lot easier - every 
# subarray we consider must contain the element immediately beside the center, which means there are only as many 
# subarrays as there are elements. In our example, the right side is [4, -2, 1]. There are only 3 subarrays to 
# consider - [4], [4, -2], and [4, -2, 1]. To find the best chain of elements we can take from a half, iterate 
# from the middle to the end (start of the array for the left half) and continuously update some counter curr.
# (check example animation)

# Algorithm:
# Now that we know how to find the best subarray containing elements from both sides of any given array, the 
# algorithm is as follows:
# 1. Define a helper function that we will use for recursion.
#   -   This function will take an input left and right, which defines the bounds of the array. The return value 
#       of this function will be the best possible subarray for the array that fits between left and right.
#   -   If left > right, we have an empty array. Return negative infinity.
#   -   Find the midpoint of our array. This is (left + right) / 2, rounded down. Using this midpoint, find the 
#       best possible subarray that uses elements from both sides of the array with the algorithm detailed in 
#       the animation above.
#   -   The best subarray using elements from both sides is only 1 of 3 possibilities. We still need to find the 
#       best subarray using only the left or right halves. So, call this function again, once with the left half, 
#       and once with the right half.
#   -   Return the largest of the 3 values - the best left half sum, the best right half sum, and the best 
#       combined sum.
# 2. Call our helper function with the entire input array (left = 0, right = length - 1). This is our final 
#       answer, so return it.


import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)



nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))


# Complexity Analysis:
# Time complexity: O(N⋅logN), where N is the length of nums.
# Space complexity: O(logN), where N is the length of nums.