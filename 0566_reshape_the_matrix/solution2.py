from collections import deque

class Solution:
    def matrixReshape(self, mat: [int], r: int, c: int) -> [int]:
        # if len(mat)==0 or r*c != len(mat) * len(mat[0]):
        #     return mat
        
        # queue = deque()
        # res=[]
        # for rows in mat:
        #     for val in rows:
        #         queue.append(val)
        
        # for i in range(r):
        #     temp=[]
        #     for i in range(c):
        #         temp.append(queue.popleft())
        #     res.append(temp)
            
        # return res

        if len(mat)==0 or r*c != len(mat) * len(mat[0]):
            return mat
        
        queue = deque()
        
        # List of lists changes reflected across sublists unexpectedly
        # https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
        # res=[[None]*c]*r
        # this is the fix
        res=[[None]*c for _ in range(r)]
        for rows in mat:
            for val in rows:
                queue.append(val)
        
        for i in range(r):
            for j in range(c):
                res[i][j]=queue.popleft()
            
        return res
            
mat = [[1,2],[3,4]]
r=4
c=1
obj = Solution()
print(obj.matrixReshape(mat,r,c))


# Complexity Analysis:
# Time complexity : O(m⋅n). We traverse over m⋅n elements twice. Here, m and n refer to the number of rows and 
# columns of the given matrix respectively.
# Space complexity : O(m⋅n). The queue formed will be of size m⋅n.