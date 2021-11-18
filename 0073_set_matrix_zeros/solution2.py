# Approach 2: O(1) Space, Efficient Solution
# Intuition:
# Rather than using additional variables to keep track of rows and columns to be reset, we use the matrix itself as the indicators.

# The idea is that we can use the first cell of every row and column as a flag. This flag would determine whether a row or column has 
# been set to zero. This means for every cell instead of going to M+N cells and setting it to zero we just set the flag in two cells.

# if cell[i][j] == 0 {
#     cell[i][0] = 0
#     cell[0][j] = 0
# }

# These flags are used later to update the matrix. If the first cell of a row is set to zero this means the row should be marked zero. 
# If the first cell of a column is set to zero this means the column should be marked zero.

# Neetcode:
# https://www.youtube.com/watch?v=T41rL0L3Pnw (used for understanding, but not for code; used leetcode solution for code)

from typing import List

class Solution(object):
    def setZeroes(self, matrix):
        
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
        
        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
print(obj.setZeroes(matrix))


# Complexity Analysis:
# Time Complexity : O(M×N)
# Space Complexity : O(1)