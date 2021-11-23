# Neetcode:
# https://youtu.be/fMSJSS7eO1w

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # define the boundaries
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                
                # shifting order in counter clockwise, so that 1 temp variable would be sufficient
                # save the topLeft
                topLeft = matrix[top][l + i]
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right in to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move top left in to top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
        return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.rotate(matrix))


# Complexity Analysis:
# Time complexity : O(n^2). We wil have to look at each cell in the matrix only once.
# Space complexity : O(1). Inplace, constant space 
