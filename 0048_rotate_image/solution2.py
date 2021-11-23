# Approach 1: Rotate Groups of Four Cells
# https://leetcode.com/problems/rotate-image/solution/

from typing import List
import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(math.ceil(n / 2)):
            for j in range(n // 2):
                
                # print(i,j)
                # print(n-1-j, i)
                # print(n-1-i, n-1-j)
                # print(j, n-1-i)
                
                
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.rotate(matrix))


# Complexity Analysis:
# Let M be the number of cells in the matrix.
# Time complexity : O(M), as each cell is getting read once and written once.
# Space complexity : O(1) because we do not use any other additional data structures.
