# Double for loop:

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        for row in matrix:
            for value in row:
                if value > target:
                    return False
                elif value == target:
                    return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 8
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(N^2)
# Space complexity : O(1) No extra space used