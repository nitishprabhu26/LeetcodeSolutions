# Approach One liners


from collections import Counter

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') == 0


# OR

class Solution:
    def checkRecord(self, s: str) -> bool:
        return Counter(s)['A'] <2 and 'LLL' not in s
        

s = "PPALLP"
obj = Solution()
print(obj.checkRecord(s))


# Complexity Analysis:
# Time complexity : O(n).
# Space complexity : O(1). No extra space is used.