# Neetcode: Iterative BFS OR Iterative DFS(by changing popleft to pop)
# https://youtu.be/pV2kpPD66nE


import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nRows, nCols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        # Iterative BFS
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # OR
                # Iterative DFS (by changing popleft to pop)
                # row, col = q.pop()

                # we can go in 4 directions: right, left, above and below
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r) in range(nRows) and
                        (c) in range(nCols) and
                        grid[r][c] == "1" and
                            (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(nRows):
            for c in range(nCols):
                # call bfs only on the node which is '1', and which is not visited yet
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
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
