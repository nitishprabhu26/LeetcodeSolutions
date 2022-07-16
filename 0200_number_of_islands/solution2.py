# Approach #2: BFS [Accepted]

# Algorithm:
# Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First 
# Search. Put it into a queue and set its value as '0' to mark as visited node. Iteratively search the neighbors 
# of enqueued nodes until the queue becomes empty.


import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    
                    # mark as visited
                    grid[r][c] = '0'
                    
                    q = collections.deque()
                    q.append((r, c))
                    while q:
                        row, col = q.popleft()
                        
                        # we can go in 4 directions: right, left, above and below
                        if (row - 1 >= 0 and grid[row - 1][col] == '1'):
                            q.append((row - 1, col))
                            grid[row - 1][col] = '0'
                            
                        if (row + 1 < nr and grid[row + 1][col] == '1'):
                            q.append((row + 1, col))
                            grid[row + 1][col] = '0'
                            
                        if (col - 1 >= 0 and grid[row][col - 1] == '1'):
                            q.append((row, col - 1))
                            grid[row][col - 1] = '0'
                            
                        if (col + 1 < nc and grid[row][col + 1] == '1'):
                            q.append((row, col + 1))
                            grid[row][col + 1] = '0'
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
# Space complexity :  O(min(M, N)) because in worst case where the grid is filled with lands, the size of queue 
# can grow up to min(M,N).