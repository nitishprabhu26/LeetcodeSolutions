# Approach #1: Depth-First Search (Recursive) [Accepted]

# Intuition and Algorithm:
# We want to know the area of each connected shape in the grid, then take the maximum of these.
# If we are on a land square and explore every square connected to it 4-directionally (and recursively squares 
# connected to those squares, and so on), then the total number of squares explored will be the area of that 
# connected shape.
# To ensure we don't count squares in a shape more than once, let's use seen to keep track of squares we haven't 
# visited before. It will also prevent us from counting the same shape more than once.


from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))


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
# call stack during our recursion.
