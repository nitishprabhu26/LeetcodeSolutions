# Approach : Using conunters
# https://docs.python.org/3/library/collections.html#collections.Counter

# dict 1 & dict 2 will intersect the two counters here, the lowest counts are preserved.
# elements() is Counter's method, it just take the elements as many times as their counts.


import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        for a in words:
            res &= collections.Counter(a)
        return list(res.elements())


# OR

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = collections.Counter(words[0])
        for s in words:
            cnt2 = collections.Counter(s)
            for k in cnt.keys():
                cnt[k] = min(cnt[k], cnt2[k])
        return cnt.elements()

        
words = ["bella","label","roller"]
obj = Solution()
print(obj.commonChars(words))


# Complexity Analysis:
# Time complexity: O(n).
# Space complexity: O(n).