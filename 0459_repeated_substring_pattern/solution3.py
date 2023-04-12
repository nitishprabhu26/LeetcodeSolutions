# Regular expression starter:
# https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
# https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/
# https://www.geeksforgeeks.org/python-re-search-vs-re-match/


# Approach 1: Regex:
# https://leetcode.com/problems/repeated-substring-pattern/solution/
# OR
# https://youtu.be/KOUtRfgslGM?t=518


import re

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = re.compile(r'^(.+)\1+$')
        return pattern.match(s)


# OR
# https://youtu.be/KOUtRfgslGM?t=518

import re
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = re.compile(r'^([a-z]+)\1+$')
        return pattern.match(s)


s = "abcabcabcabc"
obj = Solution()
print(obj.repeatedSubstringPattern(s))


# Complexity Analysis:
# Let n be the length of the input string 's'.
# Time Complexity: O(n^2), because we use greedy regex pattern. Once we have a +, the pattern is greedy.
# The difference between the greedy and the non-greedy match is the following:
# -   the non-greedy match will try to match as few repetitions of the quantified pattern as possible.
# -   the greedy match will try to match as many repetitions as possible.
# Space Complexity: O(1). We don't use any additional data structures, and everything depends on internal regex 
# implementation, which is evolving quite fast nowadays.