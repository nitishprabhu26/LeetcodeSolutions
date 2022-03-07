# Approach (Similar to approach 3) : Neetcode
# https://youtu.be/P6RZZMu_maU


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                # we could also initialize length = 1
                length = 0

                while (n + length) in numSet:
                    length += 1

                longest = max(longest, length)

        return longest
            

nums = [100,4,200,1,3,2]
obj = Solution()
print(obj.longestConsecutive(nums))


# Complexity Analysis: (Similar to Approach 3)
# Time Complexity: O(N)
# Space Complexity: O(N)