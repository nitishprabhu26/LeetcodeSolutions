# Approach : Linear time using an extra array

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows, num_cols = len(grid), len(grid[0])
        array_1D = []
        
        for i in range(num_rows):
            array_1D += grid[i]
        
        # for case where k > len(array_1D)
        k = k % len(array_1D)
        array_1D =  array_1D[-k:] + array_1D[:-k]
        array_1D = array_1D[::-1]
        
        for i in range(num_rows):
            for j in range(num_cols):
                grid[i][j] = array_1D.pop()
        
        return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
obj = Solution()
print(obj.shiftGrid(grid, k))


# Complexity Analysis:
# Time complexity : O(m.n), where the grid size is m.n.
# Space complexity : O(m.n)