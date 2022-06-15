# Approach 2: Better Counting
# OR
# https://youtu.be/FkjFlNtTzc8

# Approach 2 has the same time and space complexity as Approach 1. Even though they have the same time and space 
# complexities, Approach 2 is slightly more efficient than the Approach 1. Rather than checking 4 surrounding 
# neighbors, we only need to check two neighbors (LEFT and UP) in Approach 2.

# Intuition:
# Since we are traversing the grid from left to right, and from top to bottom, for each land cell we are currently 
# at, we only need to check whether the LEFT and UP cells are land cells with a slight modification on previous 
# approach.
# - As you go through each cell on the grid, treat all the land cells as having a perimeter of 4 and add that up 
#   to the accumulated result.
# - If that land cell has a neighboring land cell, remove 2 sides (one from each land cell) which will be touching 
#   between these two cells.
#   - If your current land cell has a UP land cell, subtract 2 from your accumulated result.
#   - If your current land cell has a LEFT land cell, subtract 2 from your accumulated result.


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
                
        
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

obj = Solution()
print(obj.islandPerimeter(grid))


# Complexity Analysis:
# Time Complexity: O(m.n) where m is the number of rows of the grid and n is the number of columns of the grid. 
# Since two for loops go through all the cells on the grid, for a two-dimensional grid of size m×n, the algorithm 
# would have to check m.n cells.
# Space Complexity: O(1). Only the result variable is updated and there is no other space requirement.

