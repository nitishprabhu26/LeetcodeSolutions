# Approach #2: Compare With Top-Left Neighbor [Accepted]

# Intuition and Algorithm:
# For each diagonal with elements in order a_1, a_2, a_3, ..... , a_k, we can check a_1 = a_2, a_2 = a_3, ..... , 
# a_{k-1} = a_k. The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to 
# bottom-right) diagonals.
# Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, 
# for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].


from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # for r, row in enumerate(matrix):
        #     for c, val in enumerate(row):
        #         if not(r == 0 or c == 0 or matrix[r - 1][c - 1] == val):
        #             return False
        # return True
        
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
        
            
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
obj = Solution()
print(obj.isToeplitzMatrix(matrix))


# Complexity Analysis:
# Time Complexity: O(M * N), where M,N are the number of rows and columns in matrix.
# Space Complexity: O(1).