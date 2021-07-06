# Iterative BFS

import collections

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
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
                # we can go in 4 directions: right, left, above and below
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if ((r) in range(nRows) and
                        (c) in range(nCols) and
                        grid[r][c] == "1" and
                            (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(nRows):
            for c in range(nCols):
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

# pending
