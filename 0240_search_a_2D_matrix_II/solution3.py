# Approach 3: Divide and Conquer

# Intuition:
# We can partition a sorted two-dimensional matrix into four sorted submatrices, two of which might contain target 
# and two of which definitely do not.

# Algorithm:
# Because this algorithm operates recursively, its correctness can be asserted via the correctness of its base and 
# recursive cases.

# Base Case:
# For a sorted two-dimensional array, there are two ways to determine in constant time whether an arbitrary element 
# target can appear in it. 
# - First, if the array has zero area, it contains no elements and therefore cannot contain target. 
# - Second, if target is smaller than the array's smallest element (found in the top-left corner) or larger than 
# the array's largest element (found in the bottom-right corner), then it definitely is not present.

# Recursive Case:
# If the base case conditions have not been met, then the array has positive area and target could potentially be 
# present. Therefore, we seek along the matrix's middle column for an index row such that 
# matrix[row-1][mid] < target < matrix[row][mid] (obviously, if we find target during this process, we immediately 
# return true). The existing matrix can be partitioned into four submatrice around this index; the top-left and 
# bottom-right submatrice cannot contain target (via the argument outlined in Base Case section), so we can prune 
# them from the search space. 
# Additionally, the bottom-left and top-right submatrice are sorted two-dimensional matrices, so we can recursively 
# apply this algorithm to them.


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid - 1, down) or \
                   search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(n.logn).
# Space complexity : O(log n). Although this approach does not fundamentally require greater-than-constant addition 
# memory, its use of recursion means that it will use memory proportional to the height of its recursion tree. 
# Because this approach discards half of matrix on each level of recursion (and makes two recursive calls), the 
# height of the tree is bounded by logn.