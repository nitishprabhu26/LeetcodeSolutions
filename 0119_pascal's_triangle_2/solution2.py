# Say we have the current layer [1, 2, 1]. We then make 2 copies of this layer, 
# add 0 to the start of one copy, and add 0 to the end of one copy; then we have [0, 1, 2, 1] and [1, 2, 1, 0]. 
# Then we can perform the element-wise add operation and we would have [1, 3, 3, 1]. 
# This is from the definition of Pascal's Triangle.

class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

row = 21
obj = Solution()
print(obj.getRow(row))