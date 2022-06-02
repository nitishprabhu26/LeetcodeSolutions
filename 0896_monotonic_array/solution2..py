# Approach 2: One Pass

# Intuition:
# To perform this check in one pass, we want to handle a stream of comparisons from {−1,0,1}, corresponding to 
# <, ==, or >. For example, with the array [1, 2, 2, 3, 0], we will see the stream (-1, 0, -1, 1).

# Algorithm:
# Keep track of store, equal to the first non-zero comparison seen (if it exists.) If we see the opposite 
# comparison, the answer is False.
# Otherwise, every comparison was (necessarily) in the set {−1,0}, or every comparison was in the set {0,1}, and 
# therefore the array is monotonic.


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        store = 0
        for i in range(len(nums) - 1):
            # (a > b) - (a < b)
            c = (nums[i] > nums[i+1]) - (nums[i] < nums[i+1])
            if c:
                if c != store and store != 0:
                    return False
                store = c
        return True
            

nums = [1,2,2,3]
nums = [6,5,4,4]
obj = Solution()
print(obj.isMonotonic(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(1)