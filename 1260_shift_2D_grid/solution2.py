# Approach 1: Simulation

# Intuition:
# In the question, we are given instructions on how to apply the transformation. Therefore, we could just repeat 
# applying the transformation k times.

# Algorithm:
# Transformations are:
# -   Element at grid[i][j] moves to grid[i][j + 1]
# -   Element at grid[i][n - 1] moves to grid[i + 1][0].
# -   Element at grid[m - 1][n - 1] moves to grid[0][0].
# Then, k times, we need to create a new 2D array and follow the given rules to move the values.


from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        num_rows, num_cols = len(grid), len(grid[0])

        for _ in range(k):
            # Create a new grid to copy into.
            new_grid = [[0] * num_cols for _ in range(num_rows)]

            # Case 1: Move everything not in the last column.
            for row in range(num_rows):
                for col in range(num_cols - 1):
                    new_grid[row][col + 1] = grid[row][col]

            # Case 2: Move everything in last column, but not last row.
            for row in range(num_rows - 1):
                 new_grid[row + 1][0] = grid[row][num_cols - 1]

            # Case 3: Move the bottom right.
            new_grid[0][0] = grid[num_rows - 1][num_cols - 1]

            grid = new_grid

        return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
obj = Solution()
print(obj.shiftGrid(grid, k))


# Complexity Analysis:
# Time complexity : O(n⋅m⋅k), where the grid size is n⋅m and we need to apply the transform k times.
# Space complexity : O(n⋅m). We are creating a new array in each iteration of the loop. We only keep track of at 
# most 2 arrays at a time, though. The rest are garbage collected/ free'd.