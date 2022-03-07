# Approach 2: Sorting

# Intuition:
# If we can iterate over the numbers in ascending order, then it will be easy to find sequences of consecutive 
# numbers. To do so, we can sort the array.

# Algorithm:
# Before we do anything, we check for the base case input of the empty array. The longest sequence in an empty 
# array is, of course, 0, so we can simply return that. For all other cases, we sort nums and consider each 
# number after the first (because we need to compare each number to its previous number). 
# If the current number and the previous are equal, then our current sequence is neither extended nor broken, 
# so we simply move on to the next number. If they are unequal, then we must check whether the current number 
# extends the sequence (i.e. nums[i] == nums[i-1] + 1). If it does, then we add to our current count and continue. 
# Otherwise, the sequence is broken, so we record our current sequence and reset it to 1 (to include the number 
# that broke the sequence). It is possible that the last element of nums is part of the longest sequence, so we 
# return the maximum of the current sequence and the longest one.


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
            

nums = [100,4,200,1,3,2]
obj = Solution()
print(obj.longestConsecutive(nums))


# Complexity Analysis:
# Time Complexity: O(nlgn).
# The main for loop does constant work n times, so the algorithm's time complexity is dominated by the invocation 
# of sort, which will run in O(nlgn) time for any sensible implementation.
# Space Complexity: O(1) (or O(n)).
# For the implementations provided here, the space complexity is constant because we sort the input array in 
# place. If we are not allowed to modify the input array, we must spend linear space to store a sorted copy.