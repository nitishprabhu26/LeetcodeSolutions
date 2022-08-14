# Approach #1 (Space Sub-Optimal) [Accepted]


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        numZeros = 0
        # Count the zeroes
        for i in range(len(nums)):
            numZeros += (nums[i] == 0)

        extraArray = []
        # Make all the non-zero elements retain their original order.
        for i in range(len(nums)):
            if nums[i] != 0:
                extraArray.append(nums[i])

        # Move all zeroes to the end
        while numZeros > 0:
            extraArray.append(0)
            numZeros -= 1

        # Assign the results back to nums variable
        nums[:] = extraArray
        return nums


nums = [0, 9, 0, 7, 0, 0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes(nums))


# Complexity Analysis:
# Space Complexity : O(n). Since we are creating the "extraArray" array to store results.
# Time Complexity: O(n).
