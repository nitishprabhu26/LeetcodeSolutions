# Approach #1 Simple Solution [Accepted]
# One simple way of solving this problem is to count number of A′s in the string and check whether the string 
# LLL is a substring of a given string. If number of A′s is less than 2 and LLL is not a subtring of a given 
# string then return true, otherwise return false.

# https://www.w3schools.com/python/ref_string_find.asp
# https://www.w3schools.com/python/ref_string_index.asp
# The index() method is almost the same as the find() method, the only difference is that the find() method 
# returns -1 if the value is not found. The index() method raises an exception if the value is not found.


class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == "A":
                count += 1
        
        return count < 2 and s.find("LLL") < 0


s = "PPALLP"
obj = Solution()
print(obj.checkRecord(s))


# Complexity Analysis:
# Time complexity : O(n). Single loop and find method takes O(n) time.
# Space complexity : O(1). Constant space is used.