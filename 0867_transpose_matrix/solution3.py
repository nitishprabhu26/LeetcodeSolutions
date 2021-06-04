# Approach 1: Copy Directly

# Transpose on main diagonal:
# The transpose of a matrix A with dimensions R x C is a matrix ans with dimensions C x R for which ans[c][r] = A[r][c].

class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        R, C = len(matrix), len(matrix[0])
        ans = [[None]*R for _ in range(C)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


# class Solution:
#     def transpose(self, matrix: [[int]]) -> [[int]]:
#         res = []
#         for i in range(len(matrix[0])):
#             temp=[]
#             for j in range(len(matrix)):
#                 temp.append(matrix[j][i])
#             res.append(temp)
#         return res


# Transpose on secondary diagonal: (different from this problem)
# class Solution:
    # def transpose(self, matrix: [[int]]) -> [[int]]:

        # reversing the list and also the list of list
        # matrix= [i[::-1] for i in matrix[::-1]]

        # res = []
        # for i in range(len(matrix[0])):
        #     temp=[]
        #     for j in range(len(matrix)):
        #         temp.append(matrix[j][i])
        #     res.append(temp)
        # return res

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# M*N matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
obj = Solution()
print(obj.transpose(matrix))


# Complexity Analysis:
# Time Complexity: O(R∗C), where R and C are the number of rows and columns in the given matrix A.
# Space Complexity: O(R∗C), the space used by the answer.
