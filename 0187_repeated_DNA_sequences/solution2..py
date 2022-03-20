# Approach 1: Linear-time Slice Using Substring + HashSet (Extra)

# https://youtu.be/89ksiltE4bQ

from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for x in range(len(s) - 9):
            if s[x: x + 10] not in d:
                d[s[x: x + 10]] = 0
            d[s[x: x + 10]] += 1
            
        return [key for key, vals in d.items() if vals > 1]

# OR

# https://youtu.be/uTmB_l-slQY

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lookup = set()
        output = set()
        N = len(s)

        for i in range(10, N + 1):
            if s[i - 10 : i] in lookup:
                output.add(s[i - 10 : i])
            lookup.add(s[i - 10 : i])
        
        return list(output)

# OR (using counter object)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)

        count = Counter(s[i - 10 : i] for i in range(10, N + 1))
        return [k for k, v in count.items() if v > 1]


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
obj = Solution()
print(obj.findRepeatedDnaSequences(s))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(N).