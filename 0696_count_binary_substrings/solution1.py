# Approach #1: Group By Character [Accepted]

# Intuition:
# We can convert the string s into an array groups that represents the length of same-character contiguous blocks 
# within the string. For example, if s = "110001111000000", then groups = [2, 3, 4, 6].
# For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, the middle of this string must occur 
# between two groups.
# Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. If we have 
# groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000". We clearly can make 
# min(groups[i], groups[i+1]) valid binary strings within this string. Because the binary digits to the left or 
# right of this string must change at the boundary, our answer can never be larger.

# Algorithm:
# Let's create groups as defined above. The first element of s belongs in it's own group. From then on, each 
# element either doesn't match the previous element, so that it starts a new group of size 1; or it does match, 
# so that the size of the most recent group increases by 1.
# Afterwards, we will take the sum of min(groups[i-1], groups[i]).


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans


# OR
# Alternate Implentation
# https://www.geeksforgeeks.org/itertools-groupby-in-python/

import itertools

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))

        
s = "00110011"
obj = Solution()
print(obj.countBinarySubstrings(s))


# Complexity Analysis:
# Time complexity : O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the 
# for-block.
# Space complexity : O(N), the space used by groups.
