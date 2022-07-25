# Approach 2: Binary Search

# Algorithm:
# First, we ensure that matrix is not null and not empty. Then, if we iterate over the matrix diagonals, we can 
# maintain an invariant that the slice of the row and column beginning at the current (row, col) pair is sorted. 
# Therefore, we can always binary search these row and column slices for target. We proceed in a logical fashion, 
# iterating over the diagonals, binary searching the rows and columns until we either run out of diagonals (meaning 
# we can return False) or find target (meaning we can return True). The binarySearch function works just like 
# normal binary search, but is made ugly by the need to search both rows and columns of a two-dimensional array.


from typing import List

class Solution:
    def binary_search(self, matrix, target, start, vertical):
        # iterate over the matrix diagonals, ignoring previous values
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(log(n!)). 
# https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
# Space complexity : O(1). Because our binary search implementation does not literally slice out copies of rows and 
# columns from matrix, we can avoid allocating greater-than-constant memory.