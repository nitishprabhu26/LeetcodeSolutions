# Approach : Neetcode
# https://youtu.be/iJGr1OtmH0c


from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
                    return 0
            visit.add((r, c))
            return (1 + dfs(r - 1, c) +
                        dfs(r + 1, c) +
                        dfs(r, c - 1) +
                        dfs(r, c + 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        
        return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution()
print(obj.maxAreaOfIsland(grid))


# OR
# Set grid[r][c] == 0 when visited, instead of cisit hashset

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0):
                    return 0
            grid[r][c] = 0
            return (1 + dfs(r - 1, c) +
                        dfs(r + 1, c) +
                        dfs(r, c - 1) +
                        dfs(r, c + 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area


# Complexity Analysis:
# Time complexity : O(R ∗ C), where R is the number of rows in the given grid, and C is the number of columns. We 
# visit every square once.
# Space complexity : O(R ∗ C), the space used by seen to keep track of visited squares, and the space used by the
# stack.
