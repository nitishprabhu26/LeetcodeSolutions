# Approach #2 Better Solution [Accepted]

# Algorithm:
# One optimization of above method is to break the loop when count of A′s becomes 2.


class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == "A":
                count += 1
            if count == 2:
                return False
        
        return s.find("LLL") < 0


s = "PPALLP"
obj = Solution()
print(obj.checkRecord(s))


# Complexity Analysis:
# Time complexity : O(n). Single loop and find method takes O(n) time.
# Space complexity : O(1). Constant space is used.