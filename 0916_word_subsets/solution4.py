# Approach: Using Counter
# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward

# Intuition:
# For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine 
# these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.


import collections
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = collections.Counter()
        for b in words2:
            count |= collections.Counter(b)
        return [a for a in words1 if not count - collections.Counter(a)]
        

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
obj = Solution()
print(obj.wordSubsets(words1, words2))


# Complexity Analysis:
# Time Complexity: O(A + B), where A and B is the total amount of information in A and B respectively.
# Space Complexity: O(A.length + B.length).
