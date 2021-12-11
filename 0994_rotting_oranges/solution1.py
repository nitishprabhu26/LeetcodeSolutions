# Neetcode:
# https://youtu.be/y704fEOx0s0

# BFS strategy prioritizes the breadth over depth, i.e. it goes wider before it goes deeper. On the other hand, 
# the DFS strategy prioritizes the depth over breadth.
# BFS is better fit here

# Algorithm:
# One of the most distinguished code patterns in BFS algorithms is that often we use a queue data structure to 
# keep track of the candidates that we need to visit during the process.
# The main algorithm is built around a loop iterating through the queue. At each iteration, we pop out an 
# element from the head of the queue. Then we do some particular process with the popped element. More 
# importantly, we then append neighbors of the popped element into the queue, to keep the BFS process running.

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize double ended queue, to implement a multi-source BFS
        # DFS wouldnt work
        q = deque()
        
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        # for the 4 directions that we can move in
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    # if in bounds and fresh, then make it rotten. else continue
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                            
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
                    
            time += 1
        
        return time if fresh == 0 else -1
        
nums = [[2,1,1],[1,1,0],[0,1,1]]
nums = [[2,1,1],[0,1,1],[1,0,1]]
nums = [[0,2]]
obj = Solution()
print(obj.orangesRotting(nums))



# Complexity Analysis:

# Time Complexity: O(n.m), where n,m are the rows and cols of the matrix. 
# or O(N) where N is size of grid. (as in leetcode solution explaination)
# First, we scan the grid to find the initial values for the queue, which would take O(N) time.
# Then we run the BFS process on the queue, which in the worst case would enumerate all the cells in the 
# grid once and only once. Therefore, it takes O(N) time.
# Thus combining the above two steps, the overall time complexity would be O(N)+O(N)=O(N)

# Space complexity : O(n.m) or O(N)
# In the worst case, the grid is filled with rotten oranges. As a result, the queue would be initialized 
# with all the cells in the grid
