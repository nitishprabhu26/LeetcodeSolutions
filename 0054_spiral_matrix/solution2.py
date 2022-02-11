# Neetcode:
# https://youtu.be/BJnMZNwUk1M


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            
            # Traverse from left to right.
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse downwards.
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not(left < right and top < bottom):
                break
            
            # Traverse from right to left.
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # Traverse upwards.
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.spiralOrder(matrix))


# Complexity Analysis:
# Let M be the number of rows and N be the number of columns.
# Time complexity : O(M.N). This is because we visit each element once.
# Space complexity : O(1). This is because we don't use other data structures. Remember that we don't include 
# the output array in the space complexity. 
