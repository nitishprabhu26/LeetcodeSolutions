# Approach 3: Using division and modulus

class Solution:
    def matrixReshape(self, mat: [int], r: int, c: int) -> [int]:
        if len(mat) == 0 or r*c != len(mat) * len(mat[0]):
            return mat

        count = 0
        res = [[None]*c for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[count//c][count % c] = mat[i][j]
                count += 1
        return res


mat = [[1, 2], [3, 4]]
r = 4
c = 1
obj = Solution()
print(obj.matrixReshape(mat, r, c))

# Complexity Analysis:
# Time complexity : O(m⋅n). We traverse the entire matrix of size m⋅n once only. Here, m and n refers to the 
# number of rows and columns in the given matrix.
# Space complexity : O(m⋅n). The resultant matrix of size m⋅n is used.