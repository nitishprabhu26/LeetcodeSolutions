# Approach 2: Depth First Search (DFS)

# Algorithm:
# DFS is very similar to BFS. Instead of using a queue and working iteratively, we'll use recursion. Our dfs 
# method will be called for every reachable cell. 
# Note: we could also work iteratively with DFS, in which case we would simply use a stack instead of a queue like 
# in the Approach 1 code, with mostly everything else being identical to the BFS approach.

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not heights or not heights[0]: 
            return []
        
        # Initialize variables, including sets used to keep track of visited cells
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        
        def dfs(row, col, reachable):
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                dfs(new_row, new_col, reachable)
        
        
        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)
        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
                    
                    

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

obj = Solution()
print(obj.pacificAtlantic(heights))

# Complexity Analysis:
# Time Complexity: O(M⋅N), where M is the number of rows and N is the number of columns.
# Similar to approach 1. The dfs function runs exactly once for each cell accessible from an ocean.
# Space Complexity: O(M⋅N), where M is the number of rows and N is the number of columns.
# Similar to approach 1. Space that was used by our queues is now occupied by dfs calls on the recursion stack.