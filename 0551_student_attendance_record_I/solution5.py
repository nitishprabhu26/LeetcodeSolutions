# Approach #4 Using Regex [Accepted]

# Algorithm:
# A regular expression is a special sequence of characters that helps you match or find other strings or sets of 
# strings, using a specialized syntax held in a pattern.

# Following are the regex's used in this solution:
# . : Matches any single character except newline.
# * : Matches 0 or more occurrences of the preceding expression.
# .* : Matches any string
# a|b : Matches either a or b


import re

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not re.search('A.*A|LLL', s)


s = "PPALLP"
obj = Solution()
print(obj.checkRecord(s))


# Complexity Analysis:
# Time complexity : O(n). Matches method takes O(n) time.
# Space complexity : O(1). N extra space is used.