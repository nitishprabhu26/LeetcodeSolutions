# Approach 3: Using Modulo Arithmetic

# Intuition:
# In addition to the pattern we observed in the previous approach, another good strategy for 2D grid problems that 
# we'll use is calculating the new locations as 2 separate steps.
# What is the new column?
# What is the new row?

# Coming up with general formulae:

# For the column, we calculated what column it'd end up in if the grid was infinite, and then we took it modulo 
# the total number of columns. As a general formula, this is:
# => new_col = (j + k) % num_cols
# Where j is the column the value starts in and num_colsnum is the total number of columns in the grid.

# The row was a little more complicated; we needed to tackle it in several parts. Firstly, we calculated how many 
# times it would move down by 1 row. Secondly, we calculated what the infinite row would be and then took that 
# modulo the number of rows. This gives us the following formula:
# => number_of_increments = (j + k) / num_cols
# => new_row = (i + number_of_increments) % num_rows


from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col + k) % num_cols
                wrap_around_count = (col + k) // num_cols
                new_row = (row + wrap_around_count) % num_rows
                new_grid[new_row][new_col] = grid[row][col]
        return new_grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
obj = Solution()
print(obj.shiftGrid(grid, k))


# Complexity Analysis:
# Time complexity : O(n⋅m), where the grid size is n⋅m. This time, we're calculating where each value moves to in 
# O(1) time instead of O(k) time. We can't do better than this in the average case, because each of the 
# n⋅m values needs to be moved to its new location.
# Space complexity : O(n⋅m). We are creating a new 2D list to write the output into.