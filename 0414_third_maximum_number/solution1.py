# Approach 1: Use a Set and Delete Maximums


from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)


nums = [3,2,1]
nums = [1,2]
obj = Solution()
print(obj.thirdMax(nums))


# Complexity Analysis:

# Time Complexity : O(n).
# Putting the input Array values into a HashSet has a cost of O(n), as each value costs O(1) to place, and there 
# are n of them.
# Finding the maximum in a HashSet has a cost of O(n), as all the values need to be looped through. We do this 
# 3 times, giving O(n). Deleting a value from a HashSet has a cost of O(1), so we can ignore this.
# In total, we're left with O(n) + O(n) = O(n).
# Space Complexity : O(n).
# In the worst case, the HashSet is the same size as the input Array, and so requires O(n) space to store.