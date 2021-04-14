# Recursion:Time limit exceeded
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        res=[]
        for i in range(rowIndex+1):
            res.append(getNum(rowIndex,i))
        return res
    
def getNum(row,col):
        if row==0 or col==0 or row==col:
            return 1
        return getNum(row-1,col-1)+getNum(row-1,col)


row = 22
obj = Solution()
print(obj.getRow(row))