# The naive approach would be to check every cell - that is, iterate through every cell, and at each one, start a 
# traversal that follows the problem's conditions. That is, find every cell that manages to reach both oceans.

# This approach, however, is extremely slow, as it repeats a ton of computation. Instead of looking for every path 
# from cell to ocean, let's start at the oceans and try to work our way to the cells. This will be much faster 
# because when we start a traversal at a cell, whatever result we end up with can be applied to only that cell. 
# However, when we start from the ocean and work backwards, we already know that every cell we visit must be 
# connected to the ocean.
# time complexity here ewould be O(M.N)^2

# Approach 1: Breadth First Search (BFS)


from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not heights or not heights[0]: 
            return []
            
        num_rows, num_cols = len(heights), len(heights[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
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
                    queue.append((new_row, new_col))
            return reachable
        
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
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