class Solution:
    def matrixReshape(self, mat: [int], r: int, c: int) -> [int]:
        new_list=[]
        result=[]
        
        for row in mat:
            for col in row:
                new_list.append(col)
        new_list=new_list[::-1]
        if len(new_list)==r*c:
            for i in range(r):
                temp_array=[]
                for j in range(c):
                    temp_array.append(new_list.pop())
                result.append(temp_array)
            return result 
        else:
            return mat
            
mat = [[1,2],[3,4]]
r=1
c=4
obj = Solution()
print(obj.matrixReshape(mat,r,c))