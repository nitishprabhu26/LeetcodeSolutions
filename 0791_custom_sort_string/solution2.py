# Approach: Sorting using lambda function
# https://youtu.be/6bmzl930ApE


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        lk = dict()
        
        i = 0
        for c in S:
            lk[c] = i
            i += 1
            
        # using large number 100 to put chars not in s to last
        # can also use 0, to put chars not in s to 0th position
        return ''.join( sorted(T, key = lambda x: lk.get(x, 100)))
# Output : cbad


# OR

from collections import defaultdict

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        lk = defaultdict(int)
        
        i = 0
        for c in S:
            lk[c] = i
            i += 1
            
        return ''.join( sorted(T, key = lambda x: lk[x]))
# Output : cdba
# No error since we use default dict, and freq of 'd' is 0
# collections.defaultdict(int) -> 'd' : 0


S = "cba"
T = "abcd"
obj = Solution()
print(obj.customSortString(S, T))


# Complexity Analysis:
# Time Complexity: O(T.log T). Used sorted.
# Space Complexity: O(S). To store frequency.