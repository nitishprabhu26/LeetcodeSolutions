class Solution:
    def generate(self, numRows: int) -> [int]:
        result=[[1]]
        if numRows==1:
            return result
        result.append([1,1])
        if numRows==2:
            return result
        for i in range(numRows-2):
            temp=[1]
            last_array=result[-1]
            for i in range(len(last_array)-1):
                temp.append(last_array[i]+last_array[i+1])
            temp.append(1)
            result.append(temp)
        return result

num = 111
obj = Solution()
print(obj.generate(num))