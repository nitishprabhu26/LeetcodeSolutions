# Approach #1 DFS [Accepted]

# Intuition:
# Treat the 2d grid map as an undirected graph and there is an edge between two horizontally or vertically adjacent 
# nodes of value '1'.

# Algorithm:
# Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. 
# During DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that 
# trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  
        def dfs(r, c):
            nr, nc = len(grid), len(grid[0])
            
            # boundary condition
            if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
                return
            
            #  every visited node should be set as '0' to mark as visited node, 
            # and call dfs on all 4 neighbors
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_islands += 1
                    
        return num_islands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
print(obj.numIslands(grid))


# Complexity analysis:
# Time complexity : O(M × N) where M is the number of rows and N is the number of columns.
# Space complexity : Worst case O(M × N) in case that the grid map is filled with lands where DFS goes by 
# M × N deep.
