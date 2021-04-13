class Solution:
    def to_add(self,arr):
        to_return=[]
        for i in range(len(arr)-1):
            to_return.append(arr[i]+arr[i+1])
        return to_return
    
    def generate(self, numRows: int) -> [int]:
        result=[[1],[1,1]]
        if numRows<3:
            return result[:numRows]
        for i in range(2,numRows):
            temp = [1] + self.to_add(result[-1]) + [1]
            result.append(temp)
        return result

num = 3
obj = Solution()
print(obj.generate(num))