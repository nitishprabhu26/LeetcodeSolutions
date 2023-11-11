# Approach: Double Binary Search without extra space
# Neetcode: https://youtu.be/Ber2pi2C0j0

# First binary search to figure out which row to search, 
# Second binary search is to find out the element in that selected row.


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1st binary search - look for the row to search
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # if none of the rows contained target value
        if not (top <= bot):
            return False
        
        # 2nd binary search - look for the target value in the selected row 
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
                
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(log(m) + log(n)) since it's a double binary search.
# Space complexity : O(1) No extra space used
