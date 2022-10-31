# Approach #1: Group by Category [Accepted]

# Intuition and Algorithm:
# - We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?
# - It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
# - This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the 
#   matrix is not Toeplitz; otherwise it is.


from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True
        
            
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
obj = Solution()
print(obj.isToeplitzMatrix(matrix))


# Complexity Analysis:
# Time Complexity: O(M * N), where M,N are the number of rows and columns in matrix.
# Space Complexity: O(M + N).