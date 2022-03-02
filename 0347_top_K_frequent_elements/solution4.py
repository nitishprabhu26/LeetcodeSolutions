# Approach Neetcode: (Using Bucket Sort)
# https://youtu.be/YPTqKIgVk-k

from typing import List
from collections import Counter


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # for index of freq, we map counts(frequency) of each value and 
        # for values of freq, we will have a list of elements which have this particular frequency
        # eg: nums = [1, 1, 1, 2, 2, 100]
        # freq = [[], [100], [2], [1], [], [], []]
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        # add top k frequent elements - in descending (most occuring first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))


# Complexity analysis:
# Time complexity : O(N). Worst case: O(N + N) if all N elements are different and each element occurs once.
# (i.e iterate through entire input array and then loop n times for index '1' since all elements hae frequency 1)
# Space complexity : O(N). Array and hashmap created.

