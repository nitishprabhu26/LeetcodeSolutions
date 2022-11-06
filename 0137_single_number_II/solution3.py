# Approach 2: HashMap

# Let's iterate over the input array to count the frequency of each number, and then return an element with a 
# frequency 1.


from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
            
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k
            
            
nums = [2,2,3,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(N) to iterate over the input array.
# Space complexity : O(N) to keep the hashmap of N/3 elements.