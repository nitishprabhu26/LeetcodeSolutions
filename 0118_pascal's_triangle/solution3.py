class Solution:
    def generate(self, numRows: int) -> [int]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            print(i)
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

num = 5
obj = Solution()
print(obj.generate(num))