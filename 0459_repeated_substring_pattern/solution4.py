# Approach 2: Concatenation
# https://leetcode.com/problems/repeated-substring-pattern/solution/

# Repeated pattern string looks like PatternPattern, and the others like Pattern1Pattern2.

# Let's double the input string:
# PatternPattern --> PatternPatternPatternPattern
# Pattern1Pattern2 --> Pattern1Pattern2Pattern1Pattern2

# Now let's cut the first and the last characters in the doubled string:
# PatternPattern --> *atternPatternPatternPatter*
# Pattern1Pattern2 --> *attern1Pattern2Pattern1Pattern*

# It's quite evident that if the new string contains the input string, the input string is a repeated pattern 
# string.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1: -1]


s = "abcabcabcabc"
obj = Solution()
print(obj.repeatedSubstringPattern(s))


# Complexity Analysis:
# Let n be the length of the input string 's'.
# Time Complexity: O(n^2), because of the way 'in' and 'contains' are implemented.
# Space Complexity: O(n). the space is implicitly used to keep s + s string.