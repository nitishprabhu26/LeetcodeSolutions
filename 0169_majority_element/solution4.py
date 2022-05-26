# Approach 4: Randomization

# Intuition:
# Because more than [n/2] array indices are occupied by the majority element, a random array index is likely to 
# contain the majority element.

# Algorithm:
# Because a given index is likely to have the majority element, we can just select a random index, check whether 
# its value is the majority element, return if it is, and repeat if it is not. The algorithm is verifiably correct 
# because we ensure that the randomly chosen value is the majority element before ever returning.


import random
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate



nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))


# Complexity Analysis:
# Time Complexity: O(∞). It is technically possible for this algorithm to run indefinitely.
# Space Complexity: O(1).