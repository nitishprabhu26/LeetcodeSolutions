# Approach 2: HashMap

# Algorithm:
# We can use a HashMap that maps elements to counts in order to count occurrences in linear time by looping over 
# nums. Then, we simply return the key with maximum value.


import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        dict={}
        for num in nums:
            dict[num] = dict.get(num,0) + 1
        for i,j in dict.items():
            if j > majority_count:
                return i
            
# OR

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        counts = collections.Counter(nums)
        
        for i,j in counts.items():
            if j > majority_count:
                return i
            
# OR

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)



nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))


# Complexity Analysis:
# Time Complexity: O(n). We iterate over nums once and make a constant time HashMap insertion on each iteration. 
# Therefore, the algorithm runs in O(n) time.
# Space Complexity: O(n). At most, the HashMap can contain n - [n/2] associations, so it occupies O(n) space.