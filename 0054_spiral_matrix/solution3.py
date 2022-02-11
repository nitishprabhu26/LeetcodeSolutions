# Approach 2: Mark Visited Elements

# Intuition
# If we mark the cells that we have visited, then when we run into a visited cell, we know we need to turn.

# How do we know which direction we need to turn to? We always follow this loop: right, down, left, up, right 
# again, and so on. Therefore, when we run into a cell that we have visited, we can simply turn to the next 
# direction in the aforementioned loop.

# Note that elements in the matrix are constrained to -100 <= matrix[row][col] <= 100, therefore we can select 
# a number that is out of this range to mark it i.e. 101 is selected for marking purposes.

# If we reach the visited cell, we need to turn. However, when we meet another visited cell immediately after 
# changing the direction, it means we reached the last element in the matrix.


# Algorithm

# Initializations:
#     - Initialize a 2D array directions to represent the four directions that we will move.
#     - Initialize currentDirection to 0 to signify that we are moving right at the beginning.
#     - Initialize VISITED to 101 to mark visited cells.
#     - Initialize changeDirection to 0.
#     - Initialize row and col to 0 since our initial position is (0, 0).
# We follow the current direction until we reach the matrix boundaries or a visited cell.
#     - While traversing in the current direction, remember to reset changeDirection to 0 at every step.
#     - Move to the next cell by updating the row and column indices.
#     - Append the element to the result and mark the location as visited.
# Update the direction and changeDirection. If changeDirection is larger than 1, it means we are continuously 
# changing our directions, and therefore we've visited all of the elements.


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right. (1 - down, 2 - left, 3 - up)
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
print(obj.spiralOrder(matrix))


# Complexity Analysis:
# Let M be the number of rows and N be the number of columns.
# Time complexity : O(M.N). This is because we visit each element once.
# Space complexity : O(1). This is because we don't use other data structures. Remember that we don't include 
# the output array in the space complexity. 
# However, if we were prohibited from mutating the input matrix, then this would be an O(M⋅N) space solution.
# This is because we would need to use a boolean matrix to track all of the previously seen cells.
