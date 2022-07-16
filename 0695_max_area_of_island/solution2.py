# Approach #2: Depth-First Search (Iterative) [Accepted]

# Intuition and Algorithm:
# We can try the same approach using a stack based, (or "iterative") depth-first search.
# Here, seen will represent squares that have either been visited or are added to our list of squares to visit 
# (stack). For every starting land square that hasn't been visited, we will explore 4-directionally around it, 
# adding land squares that haven't been added to seen to our stack.
# On the side, we'll keep a count shape of the total number of squares seen during the exploration of this shape. 
# We'll want the running max of these counts.


from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans


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


# Complexity Analysis:
# Time complexity : O(R ∗ C), where R is the number of rows in the given grid, and C is the number of columns. We 
# visit every square once.
# Space complexity : O(R ∗ C), the space used by seen to keep track of visited squares, and the space used by the
# stack.
