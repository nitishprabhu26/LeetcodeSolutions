# Approach 2: Linear Transformation
# https://youtu.be/fkSq0QE5C_0 (preferred)
# OR
# https://leetcode.com/problems/image-overlap/solution/

# Algorithm:
# The algorithm can be implemented in two overall steps.
# - First, we filter out those non-zero cells in each matrix respectively.
# - Second, we do a cartesian product on the non-zero cells. For each pair of the products, we calculate the 
#   corresponding linear transformation vector as V_{ab} = (X_b - X_a, Y_b - Y_a). 
#   Then, we count the number of the pairs that have the same transformation vector, which is also the number of 
#   ones in the overlapping zone.


from collections import Counter, defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a_1 = []
        b_1 = []
        A = img1
        B = img2
        
        # First, we filter out those non-zero cells in each matrix respectively.
        # Iterate through each of the matrices, and add the positions of non zero elements
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a_1.append((i, j))
                if B[i][j] == 1:
                    b_1.append((i, j))
                    
        d = {}
        ans = 0
        
        # Second, we do a cartesian product on the non-zero cells.
        for a_x, a_y in a_1:
            for b_x, b_y in b_1:
                translation = (b_x - a_x, b_y - a_y)
                if translation in d:
                    d[translation] += 1
                else:
                    d[translation] = 1
                ans = max(ans, d[translation])
                
        return ans


# OR
# https://leetcode.com/problems/image-overlap/solution/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = img1
        B = img2

        dim = len(A)

        def non_zero_cells(M):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)

        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps


# OR
# https://youtu.be/91S7zABWecc?t=296
# in short

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = img1
        B = img2

        n = len(A)
        # First, we filter out those non-zero cells in each matrix respectively.
        a1 = [(i, j) for i in range(n) for j in range(n) if A[i][j]]
        b1 = [(i, j) for i in range(n) for j in range(n) if B[i][j]]
        
        # Second, we do a cartesian product on the non-zero cells.
        cnt = Counter((xa - xb, ya - yb) for xa, ya in a1 for xb, yb in b1)

        return max(cnt.values() or [0])


img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]
obj = Solution()
print(obj.largestOverlap(img1, img2))


# Complexity Analysis:
# Let M_a, M_b be the number of non-zero cells in the matrix A and B respectively. 
# Let N be the width of the matrix.
# Time Complexity: O(N^4).
# - In the first step, we filter out the non-zero cells in each matrix, which would take O(N^2) time.
# - In the second step, we enumerate the cartesian product of non-zero cells between the two matrices, which would 
#   take O(M_a . M_b) time. In the worst case, both M_a and M_b would be up to N^2, i.e. matrix filled with ones.
# - To sum up, the overall time complexity of the algorithm would be O(N^2) + O(N^2 . N^2) = O(N^4).
# - Although this approach has the same time complexity as the previous approach, it should run faster in practice,
#   since we ignore those zero cells. 
# Space Complexity: O(N^2). 
# We kept the indices of non-zero cells in both matrices. In the worst case, we would need the {O}(N^2) space for 
# the matrices filled with ones.