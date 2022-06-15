# Approach : Neetcode (DFS)
# https://youtu.be/fISIuAFRM2s


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        
        def dfs(i, j):
            # base cases
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            
            visit.add((i, j))
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            
            return perim
        
        # find a cell which is island, to start with
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
                
        
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

obj = Solution()
print(obj.islandPerimeter(grid))


# Complexity Analysis:
# Time Complexity: O(m.n) where m is the number of rows of the grid and n is the number of columns of the grid. 
# Since two for loops go through all the cells on the grid, for a two-dimensional grid of size m×n, the algorithm 
# would have to check m.n cells in worst case. We will visit each cell in grid once or maybe twice.
# Space Complexity: O(m.n). We might end up adding every single item in grid to visit set

