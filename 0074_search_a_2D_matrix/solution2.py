# Approach 1: Binary Search without extra space
# One could notice that the input matrix m x n could be considered as a sorted array of length m x n.

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(log(mn)) since it's a standard binary search.
# Space complexity : O(1) No extra space used