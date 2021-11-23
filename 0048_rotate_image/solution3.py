# Approach 2: Reverse on Diagonal and then Reverse Left to Right
# Intuition
# The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal, and then reverse it 
# from left to right. These operations are called transpose and reflect in linear algebra.

from typing import List
import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Reverse
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-1-j], matrix[i][j]
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.rotate(matrix))


# Complexity Analysis:
# Let M be the number of cells in the matrix.
# Time complexity : O(M). We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a 
# cost of O(M) because we're moving the value of each cell once. Reversing each row also has a cost of O(M), because again we're 
# moving the value of each cell once.
# Space complexity : O(1) because we do not use any other additional data structures.
