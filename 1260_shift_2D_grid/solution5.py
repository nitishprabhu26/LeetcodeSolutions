# Approach : Neetcode
# https://youtu.be/nJYFh4Dl-as


from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        # convert 2D value to 1D value
        def posToVal(r, c):
            return r * N + c
        
        # convert 1D value to 2D value
        def valToPos(v):
            return [v // N, v % N] # r, c

        res = [[0] * N for i in range(M)]

        for r in range(M):
            for c in range(N):
                newValIndex = (posToVal(r, c) + k) % (M * N)
                newR, newC = valToPos(newValIndex)
                res[newR][newC] = grid[r][c]
        return res


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
obj = Solution()
print(obj.shiftGrid(grid, k))


# Complexity Analysis:
# Time complexity : O(n⋅m), where the grid size is n⋅m.
# Space complexity : O(1).