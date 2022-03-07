# Approach 1: Brute Force

# Intuition:
# Because a sequence could start at any number in nums, we can exhaust the entire search space by building as 
# long a sequence as possible from every number.

# Algorithm:
# The brute force algorithm does not do anything clever - it just considers each number in nums, attempting to 
# count as high as possible from that number using only numbers in nums. After it counts too high (i.e. currentNum 
# refers to a number that nums does not contain), it records the length of the sequence if it is larger than the 
# current best. The algorithm is necessarily optimal because it explores every possibility.


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
            

nums = [100,4,200,1,3,2]
obj = Solution()
print(obj.longestConsecutive(nums))


# Complexity Analysis:
# Time Complexity: O(N^3)
# The outer loop runs exactly n times, and because currentNum increments by 1 during each iteration of the while 
# loop, it runs in O(n) time. Then, on each iteration of the while loop, an O(n) lookup in the array is performed. 
# Therefore, this brute force algorithm is really three nested O(n) loops, which compound multiplicatively to a 
# cubic runtime.
# Space Complexity: O(1)
# The brute force algorithm only allocates a handful of integers, so it uses constant additional space.