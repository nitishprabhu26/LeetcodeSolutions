# Approach 3: In-Place

# Intuition:
# If we want to do the sort in-place, we can use quicksort, a standard textbook algorithm.

# Algorithm:
# We'll maintain two pointers i and j. The loop invariant is everything below i has parity 0 (ie. A[k] % 2 == 0 
# when k < i), and everything above j has parity 1.
# Then, there are 4 cases for (A[i] % 2, A[j] % 2):
# - If it is (0, 1), then everything is correct: i++ and j--.
# - If it is (1, 0), we swap them so they are correct, then continue.
# - If it is (0, 0), only the i place is correct, so we i++ and continue.
# - If it is (1, 1), only the j place is correct, so we j-- and continue.
# Throughout all 4 cases, the loop invariant is maintained, and j-i is getting smaller. So eventually we will be 
# done with the array sorted as desired.


from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 == 1: j -= 1

        return nums


nums = [3,1,2,4]
obj = Solution()
print(obj.sortArrayByParity(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums. Each step of the while loop makes j-i decrease by at least 
# one. (Note that while quicksort is O(NlogN) normally, this is O(N) because we only need one pass to sort the 
# elements.)
# Space Complexity: O(1) in additional space complexity.


# OR ( 2 pointer: O(n) and inplace)
# https://youtu.be/fexvdMMXNVM


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            # move left pointer until we find odd number
            while nums[l] % 2 == 0 and l < r:
                l += 1
            # move right pointer until we find even number
            while nums[r] % 2 == 1 and l < r:
                r -= 1      
            # swap
            nums[l], nums[r] = nums[r], nums[l]

        return nums