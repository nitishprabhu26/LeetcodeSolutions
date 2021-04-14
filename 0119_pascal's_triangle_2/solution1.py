class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        result=[[1],[1,1]]
        if rowIndex<2:
            return result[rowIndex]
        result=result[-1]
        for i in range(2,rowIndex+1):
            result=[1] + [ result[j]+result[j+1] for j in range(len(result)-1)] +[1]
        return result

row = 21
obj = Solution()
print(obj.getRow(row))