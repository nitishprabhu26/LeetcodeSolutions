# Approach 1: Simple Iteration
# https://leetcode.com/problems/shuffle-the-array/solution/

# Algorithm:
# 1. Build an array result of size 2 * n.
# 2. Iterate over the nums array ranging from indices 0 to n - 1:
#    -  Store the element x_i+1, that is, nums[i] at index 2 * i,
#       and element y_i+1, that is, nums[i + n] at index 2 * i + 1 in result.
# 3. Return the result array.


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[n + i]
        return result


nums = [2,5,1,3,4,7]
n = 3
obj = Solution()
print(obj.shuffle(nums, n))


# Complexity Analysis:
# Here, 2∗n is the number of elements in the nums array.
# Time complexity: O(n). 
#   -   We iterate on n elements of the nums array, which takes us O(n) time.
#   -   Initializing the result array will take O(2n) time.
#   -   Thus, overall we take O(n + 2n) = O(n) time.
# Space complexity: O(1).
#   -   We are not using any additional space other than the output array.