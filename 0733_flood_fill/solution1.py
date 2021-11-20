from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curColor = image[sr][sc]
        if curColor == newColor:
            return image
        
        R, C = len(image), len(image[0])
        
        def dfs(r, c):
            if image[r][c] == curColor:
                image[r][c] = newColor
                # going left
                if r >= 1: dfs(r-1, c)
                # going right
                if r < R-1: dfs(r+1, c)
                # going up
                if c >= 1: dfs(r, c-1)
                # going down
                if c < C-1: dfs(r, c+1)
        
        dfs(sr,sc)
        return image
            
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
obj = Solution()
print(obj.floodFill(image, sr, sc, newColor))
