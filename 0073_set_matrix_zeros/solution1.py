# Having a copy of the array woud take O(m.n) extra memory

# Approach 1: Additional Memory Approach
# Intuition:
# If any cell of the matrix has a zero we can record its row and column number. All the cells of this recorded row and column can be 
# marked zero in the next iteration.


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        # inplace of below code
            
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return matrix

        # or 
        
        # for i in rows:
        #     for col in range(C):
        #         matrix[i][col] = 0
            
        # for j in cols:
        #     for row in range(R):
        #         matrix[row][j] = 0
                    

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
print(obj.setZeroes(matrix))


# Complexity Analysis:
# Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
# Space Complexity: O(M + N).