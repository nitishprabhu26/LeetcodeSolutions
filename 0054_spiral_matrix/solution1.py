# Approach 1: Set Up Boundaries

# Algorithm:
# - Initialize the top, right, bottom, and left boundaries as up, right, down, and left.
# - Initialize the output array result.
# - Traverse the elements in spiral order and add each element to result:
#   -   Traverse from left boundary to right boundary.
#   -   Traverse from up boundary to down boundary.
#   -   Before we traverse from right to left, we need to make sure that we are not on a row that has already 
#       been traversed. If we are not, then we can traverse from right to left.
#   -   Similarly, before we traverse from bottom to top, we need to make sure that we are not on a column that 
#       has already been traversed. Then we can traverse from down to up.
#   -   Remember to move the boundaries by updating left, right, up, and down accordingly.
# - Return result


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1
        
        while len(result) < rows * columns:
            
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.spiralOrder(matrix))


# Complexity Analysis:
# Let M be the number of rows and N be the number of columns.
# Time complexity : O(M.N). This is because we visit each element once.
# Space complexity : O(1). This is because we don't use other data structures. Remember that we don't include 
# the output array in the space complexity. 
