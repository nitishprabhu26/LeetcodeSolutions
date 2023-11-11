# Approach 1: Binary Search without extra space
# One could notice that the input matrix m x n could be considered as a sorted array of length m x n.
# Sorted array is a perfect candidate for the binary search because the element index in this virtual array (for 
# sure we're not going to construct it for real) could be easily transformed into the row and column in the 
# initial matrix
# row = idx // n and col = idx % n.

# Algorithm:
# The algorithm is a standard binary search :
# - Initialise left and right indexes left = 0 and right = m x n - 1.
# - While left <= right :
#   -   Pick up the index in the middle of the virtual array as a pivot index : pivot_idx = (left + right) / 2.
#   -   The index corresponds to row = pivot_idx // n and col = pivot_idx % n in the initial matrix, and hence 
#       one could get the pivot_element. This element splits the virtual array in two parts.
#   -   Compare pivot_element and target to identify in which part one has to look for target.


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
# Time complexity : O(log(m.n)) since it's a standard binary search.
# Space complexity : O(1) No extra space used