# Approach 1: Brute Force

# Algorithm:
# We loop over the array, checking each element in turn. If we find it, we return true. Otherwise, if we reach the 
# end of the nested for loop without returning, we return false.


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
obj = Solution()
print(obj.searchMatrix(matrix, target))


# Complexity Analysis:
# Time complexity : O(n.m). Becase we perform a constant time operation for each element of an n × m element matrix,
# the overall time complexity is equal to the size of the matrix.
# Space complexity : O(1). The brute force approach does not allocate more additional space than a handful of 
# pointers, so the memory footprint is constant.