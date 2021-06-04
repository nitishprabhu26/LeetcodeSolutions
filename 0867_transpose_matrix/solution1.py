# Using zip method:

# Transpose on main diagonal:
class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        return list(zip(*matrix))


# Transpose on secondary diagonal: (different from this problem)
# class Solution:
#     def transpose(self, matrix: [[int]]) -> [[int]]:
#         return list(zip(*matrix[::-1]))[::-1]


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# M*N matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
obj = Solution()
print(obj.transpose(matrix))
