# Approach 1: Sort by Row

# Algorithm:
# We min(numRows,len(s)) lists to represent the non-empty rows of the Zig-Zag Pattern.
# Iterate through s from left to right, appending each character to the appropriate row. The appropriate row can 
# be tracked using two variables: the current row and the current direction.
# The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        # wrong way: refers each subarray to same memory
        # rows = [[]] * min(len(s), numRows)
        # rows[0].append(1)
        # print(rows) - [[1], [1], [1]]
        
        rows = []
        # define number of rows needed by appending them
        for _ in range(min(len(s), numRows)):
            rows.append([])
        
        curRow = 0
        goingDown = False
        
        for c in s:
            rows[curRow].append(c)
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
            
        res = ""
        for row in rows:
            res += ''.join(row)
        return res


# OR

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

        
s = "PAYPALISHIRING"
numRows = 3
obj = Solution()
print(obj.convert(s, numRows))


# Complexity Analysis:
# Time complexity: O(n), where n == len(s).
# Space complexity: O(n).