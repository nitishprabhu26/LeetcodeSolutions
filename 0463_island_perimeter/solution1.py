# Approach 1: Simple Counting

# Intuition:
# Go through every cell on the grid and whenever you are at cell 1 (land cell), look for surrounding (UP, RIGHT, 
# DOWN, LEFT) cells. A land cell without any surrounding land cell will have a perimeter of 4. Subtract 1 for each 
# surrounding land cell.
# When you are at cell 0 (water cell), you don't need to do anything. Just proceed to another cell.


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r-1][c]
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c-1]
                    if r == rows-1:
                        down = 0
                    else:
                        down = grid[r+1][c]
                    if c == cols-1:
                        right = 0
                    else:
                        right = grid[r][c+1]
                        
                    result += 4-(up+left+right+down)
                
        return result
                
        
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

obj = Solution()
print(obj.islandPerimeter(grid))


# Complexity Analysis:
# Time Complexity: O(m.n) where m is the number of rows of the grid and n is the number of columns of the grid. 
# Since two for loops go through all the cells on the grid, for a two-dimensional grid of size m×n, the algorithm 
# would have to check m.n cells.
# Space Complexity: O(1). Only the result variable is updated and there is no other space requirement.

