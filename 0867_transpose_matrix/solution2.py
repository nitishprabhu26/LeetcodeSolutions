# Only for M*M mproblem (same number of rows and columns)
# (Not solution for this leetcode problem as this problem is M*N matrix as input)

# Transpose on main diagonal:
class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


# Transpose on secondary diagonal: (different from this problem)
# class Solution:
#     def transpose(self, matrix: [[int]]) -> [[int]]:
#         n = len(matrix)
#         for i in range(n):
#             for j in range(n-1-i):
#                 # remember line20
#                 matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
#         return matrix

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2], [3, 4]]
obj = Solution()
print(obj.transpose(matrix))
