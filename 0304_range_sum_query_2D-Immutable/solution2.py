# Approach #2 (Caching) [Memory Limit Exceeded / Time Limit Exceeded]

# Intuition:
# Since sumRegion could be called many times, we definitely need to do some pre-processing.

# Algorithm:
# We could trade in extra space for speed by pre-calculating all possible rectangular region sum and store them 
# in a hash table. Each sumRegion query now takes only constant time complexity.


from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
        self.dict = {}
        for row1 in range(len(matrix)):
            for col1 in range(len(matrix[0])):
                for row2 in range(row1, len(matrix)):
                    for col2 in range(col1, len(matrix[0])):
                        self.dict[(row1, col1, row2, col2)] = self.findSum(row1, col1, row2, col2)
                    

    def findSum(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.data[i][j]
        return sum
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dict[(row1, col1, row2, col2)]


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
for row1, col1, row2, col2 in [[2,1,4,3],[1,1,2,2],[1,2,2,4]]:
    print(obj.sumRegion(row1,col1,row2,col2))


# Complexity Analysis
# Time Complexity: O(1) time per query, O(m^3.n^3) time pre-computation. Each sumRegion query takes O(1) time as 
# the hash table lookup's time complexity is constant. The pre-computation will take O(m^3.n^3) time as there are 
# a total of m^2 * n^2(Not sure) possibilities need to be cached.
# Space Complexity(Not sure) : O(m^3.n^3) max. Since there are m.n different possibilities for both top left and 
# bottom right points of the rectangular region, the extra space required is O(m^3.n^3)

