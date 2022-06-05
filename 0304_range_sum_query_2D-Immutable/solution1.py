# Approach #1 (Brute Force) [Time Limit Exceeded]

# Algorithm:
# Each time sumRegion is called, we use a double for loop to sum all elements from (row1, col1) -> (row2, col2).


from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.data = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.data[i][j]
        return sum


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
for row1, col1, row2, col2 in [[2,1,4,3],[1,1,2,2],[1,2,2,4]]:
    print(obj.sumRegion(row1,col1,row2,col2))


# Complexity Analysis
# Time Complexity:O(m.n) time per query. Assume that mm and nn represents the number of rows and columns 
# respectively, each sumRegion query can go through at most m×n elements.
# Space Complexity : O(1). Note that data is a reference to matrix and is not a copy of it.

