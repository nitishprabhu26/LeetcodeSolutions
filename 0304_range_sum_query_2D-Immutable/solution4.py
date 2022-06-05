# Approach #4 (Caching Smarter) [Accepted]

# Algorithm:
# We used a cumulative sum array in the 1D version. We notice that the cumulative sum is computed with respect to 
# the origin at index 0. Extending this analogy to the 2D case, we could pre-compute a cumulative region sum with 
# respect to the origin at (0, 0).

# https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
# Sum(ABCD) = Sum(OD) − Sum(OB) − Sum(OC) + Sum(OA)

# OR
# Neetcode : (kind of similar way)
# https://youtu.be/KE8MQuwE2yA


from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        # we do it the way its shown above, because the below way has an issue
        # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
for row1, col1, row2, col2 in [[2,1,4,3],[1,1,2,2],[1,2,2,4]]:
    print(obj.sumRegion(row1,col1,row2,col2))


# Complexity Analysis
# Time Complexity: O(1) time per query, O(mn) time pre-computation. The pre-computation in the constructor 
# takes O(mn) time. Each sumRegion query takes O(1) time.
# Space Complexity : O(mn). The algorithm uses O(mn) space to store the cumulative region sum.