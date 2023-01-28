# Approach #3 Single pass Solution (Without find method) [Accepted]

# Algorithm:
# We can solve this problem in a single pass without using find method. In a single loop we can count number of 
# A′s and also check the substring LLL in a given string.


class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        for i in range(len(s)):
            if s[i] == "A":
                countA += 1
            if i <= len(s) - 3 and s[i] == "L" and s[i + 1] == "L" and s[i + 2] == "L":
                return False
        
        return countA < 2


s = "PPALLP"
obj = Solution()
print(obj.checkRecord(s))


# Complexity Analysis:
# Time complexity : O(n). Single loop upto string length is used.
# Space complexity : O(1). Constant space is used.