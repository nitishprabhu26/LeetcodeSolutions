# Approach 1: Double Binary Search without extra space
# First binary search to figure out which row to search, second binary search is to find out the element in that 
# selected row.
# https://youtu.be/Ber2pi2C0j0


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])

        # binary search
        top, bottom = 0, rows-1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not top <= bottom:
            return False

        left, right = 0, columns-1
        while left <= right:
            pivot = (left + right) // 2
            if target == matrix[row][pivot]:
                return True
            elif target > matrix[row][pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(log(m) + log(n)) since it's a double binary search.
# Space complexity : O(1) No extra space used
