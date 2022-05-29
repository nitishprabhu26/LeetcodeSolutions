# Approach #2 HashSet [Accepted]

# Algorithm:
# This algorithm is almost identical to the brute force approach, except we first insert each element of nums into 
# a set, allowing us to later query for containment in O(1) time


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


# OR


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return set(range(0,len(nums)+1)).difference(set(nums)).pop() 


nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))


# Complexity Analysis
# Time complexity : O(n). 
# Because the set allows for O(1) containment queries, the main loop runs in O(n) time. Creating num_set costs 
# O(n) time, as each set insertion runs in amortized O(1) time, so the overall runtime is O(n+n) = O(n).
# Space complexity : O(n).
# nums contains n−1 distinct elements, so it costs O(n) space to store a set containing all of them.