# Neetcode: https://youtu.be/s-VkcjHqkGI

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # hashsets to store positions which can reach pacific and atlantic respectively
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            # if a position is previously visited(answer is added to hashset already), then we dont need to revisit it again: avoid redundancy
            # or if its outofbounds, then dont continue
            # or if previous height is greater than current height, then dont contiue
            if ((r, c) in visit or 
               r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
            
        # going throgh every single columns in the first(pacific) and last(atlantic) rows
        for c in range(COLS):
            # 1st row
            dfs(0, c, pac, heights[0][c])
            # last row
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
            
        # similarly going throgh every single rows in the first(pacific) and last(atlantic) columns
        for r in range(ROWS):
            # 1st column
            dfs(r, 0, pac, heights[r][0])
            # last column
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        res = []
        # until here, we already have marked every single cell which can reach pacific and atrlantic ocean respectively
        # now loop throgh all cells, and find which positions can reach both pacific and atlantic oceans
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
                    

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

obj = Solution()
print(obj.pacificAtlantic(heights))

# Complexity Analysis:
# Time Complexity: O(M⋅N), where M is the number of rows and N is the number of columns.
# Similar to approach 1. The dfs function runs exactly once for each cell accessible from an ocean.
# Space Complexity: O(M⋅N), where M is the number of rows and N is the number of columns.
# Similar to approach 1. Space that was used by our queues is now occupied by dfs calls on the recursion stack.