# Approach 3: HashSet and Intelligent Sequence Building

# Intuition:
# It turns out that our initial brute force solution was on the right track, but missing a few optimizations 
# necessary to reach O(n) time complexity.

# Algorithm:
# This optimized algorithm contains only two changes from the brute force approach 1: 
# - the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups, 
# - and we only attempt to build sequences from numbers that are not already part of a longer sequence. This is 
# accomplished by first ensuring that the number that would immediately precede the current number in a sequence 
# is not present, as that number would necessarily be part of a longer sequence. 
# (check if the current number has a left neighbor, and if no left neighbour then proceed to the while loop. 
# This also means that the current number is the start of sequence, if it has no left neighbor)


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
            

nums = [100,4,200,1,3,2]
obj = Solution()
print(obj.longestConsecutive(nums))


# Complexity Analysis:
# Time Complexity: O(N)
# Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer 
# inspection reveals it to be linear. Because the while loop is reached only when currentNum marks the beginning 
# of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for nn iterations 
# throughout the entire runtime of the algorithm. This means that despite looking like O(n⋅n) complexity, the 
# nested loops actually run in O(n + n) = O(n) time. All other computations occur in constant time, so the 
# overall runtime is linear.
# Space Complexity: O(N)
# In order to set up O(1) containment lookups, we allocate linear space for a hash table to store the O(n) 
# numbers in nums. Other than that, the space complexity is identical to that of the brute force solution.

# Time complexity explaination: why O(n) and not O(n^2)?
# take a close look at the entering of the logic: 'if num - 1 not in num_set:'
# That means, for example, 6,5,4,3,2,1 input, only the value 1 is valid for the loop(all other values have its 
# value - 1 in the set), that is O(n).
# The trick is that initial condition prevents it from iterating on every entry, but iterates only for the 
# beginning of each sequence, and all sequences can at max add up to the length of the original array.