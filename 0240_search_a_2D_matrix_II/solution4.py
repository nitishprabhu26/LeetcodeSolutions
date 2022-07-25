# Approach 4: Search Space Reduction
# OR
# using top right as starting point: https://youtu.be/dcTJRw1704w

# Intuition
# Because the rows and columns of the matrix are sorted (from left-to-right and top-to-bottom, respectively), we 
# can prune O(m) or O(n) elements when looking at any particular value.

# Algorithm:
# First, we initialize a (row, col) pointer to the bottom-left of the matrix. Then, until we find target and 
# return 'true' (or the pointer points to a (row, col) that lies outside of the dimensions of the matrix), we do 
# the following: 
# If the currently-pointed-to value is larger than target we can move one row "up". 
# Otherwise, if the currently-pointed-to value is smaller than target, we can move one column "right". 
# It is not too tricky to see why doing this will never prune the correct answer; because the rows are sorted from 
# left-to-right, we know that every value to the right of the current value is larger. Therefore, if the current 
# value is already larger than target, we know that every value to its right will also be too large. A very 
# similar argument can be made for the columns, so this manner of search will always find target in the matrix 
# (if it is present).


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(n + m)
# The key to the time complexity analysis is noticing that, on every iteration (during which we do not return true) 
# either row or col is is decremented/incremented exactly once. Because row can only be decremented m times and col 
# can only be incremented n times before causing the while loop to terminate, the loop cannot run for more than 
# n + m iterations. Because all other work is constant, the overall time complexity is linear in the sum of the 
# dimensions of the matrix.
# Space complexity : O(1). Because this approach only manipulates a few pointers, its memory footprint is constant.