# Approach 2: Visit by Row (skipped)
# Approach : Neetcode (https://youtu.be/Q2Tw6gcVEwc)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            # i tells us which position we are in the string
            # we start at r i.e. row 0 starts at 0, row 1 starts at 1 and so on
            for i in range(r, len(s), increment):
                res += s[i]
                # for in between rows(other than 1st and last rows), which has extra values
                # and also the extra charecter condition: size of the 'V' decreases by 2 each time
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res
                    

s = "PAYPALISHIRING"
numRows = 3
obj = Solution()
print(obj.convert(s, numRows))


# Complexity Analysis:
# Time complexity: O(n), where n == len(s). Each index is visited once.
# Space complexity: O(n).