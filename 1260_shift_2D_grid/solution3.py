# Approach 2: Simulation, Recycling Same Array

# Intuition:
# The previous approach created k new arrays. We can simplify it to do the movements in-place.
# Let's look at how an individual value moves around the grid. The movement is a straightforward pattern. The 
# value moves in "reading" order, and then when it gets to the bottom right, it wraps around to the top left.
# https://leetcode.com/problems/shift-2d-grid/solution/ (animation)


from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows, num_cols = len(grid), len(grid[0])

        for _ in range(k):

            previous = grid[-1][-1]
            for row in range(num_rows):
                for col in range(num_cols):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
        return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
obj = Solution()
print(obj.shiftGrid(grid, k))


# Complexity Analysis:
# Time complexity : O(n⋅m⋅k), where the grid size is n⋅m and we need to apply the transform k times.
# Space complexity : Depends on whether or not the input/ output types are the same. 
# - If the input and output are the same type (Python and C++): O(1). We aren't creating any new data structures.
# - If the input and output are different types (Java): O(n⋅m). We're creating a single n x m 2D list.