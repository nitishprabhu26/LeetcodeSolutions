# Approach #3 (Caching Rows) [Accepted]

# Intuition:
# Remember from the 1D version where we used a cumulative sum array? Could we apply that directly to solve this 
# 2D version?

# Algorithm:
# Try to see the 2D matrix as m rows of 1D arrays. To find the region sum, we just accumulate the sum in the 
# region row by row.


from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix))]
        # we do it the way its shown above, because the below way has an issue
        # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        # self.dp = [[0] * (len(matrix[0]) + 1)] * len(matrix)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            sum += self.dp[row][col2 + 1] - self.dp[row][col1]
        return sum


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
for row1, col1, row2, col2 in [[2,1,4,3],[1,1,2,2],[1,2,2,4]]:
    print(obj.sumRegion(row1,col1,row2,col2))


# Complexity Analysis
# Time Complexity:O(1) time per query, O(m^2.n^2) time pre-computation. Each sumRegion query takes O(1) time as 
# the hash table lookup's time complexity is constant. The pre-computation will take O(m^2.n^2) time as there are 
# a total of m^2 * n^2 possibilities need to be cached.
# Space Complexity : O(m^2.n^2). Since there are m.n different possibilities for both top left and bottom right 
# points of the rectangular region, the extra space required is O(m^2.n^2).
