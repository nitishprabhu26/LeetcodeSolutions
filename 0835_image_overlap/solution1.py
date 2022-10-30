# Approach: Shift and Count [Brute Force]

# Intuition:
# As stated in the problem description, in order to calculate the number of ones in the overlapping zone, we should 
# first shift one of the images. Once the image is shifted, it is intuitive to count the numbers.
# Therefore, a simple idea is that one could come up all possible overlapping zones, by shifting the image matrix, 
# and then simply count within each overlapping zone.


# https://youtu.be/Jzs2_6qf78c [Time Limit Exceeded] (Not clear) [directions mentioned for x axis is incorrect]
# moving matrix on +y = 1, and on +x = -1 (check with example)
# similarly, moving matrix on -y = -1, and on -x = +1
# [same with other below solution]


from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        largest_overlap = 0
                
        def overlap_ones(A, B, rowOff, colOff):
            count = 0
            # count the ones in each overlapping zone
            for row in range(n):
                for col in range(n):
                    if (row + rowOff <0 or row + rowOff >= n) or (col + colOff <0 or col + colOff >= n):
                        continue
                    if A[row][col] + B[row + rowOff][col + colOff] == 2:
                        count += 1       
            return count
        
        # loop over all possible combinations of shifting coordinates (x_shift, y_shift)
        # More specifically, the ranges of x_shift and y_shift are both [-n+1, n-1].
        # covering all directions
        for row_off in range(-n + 1, n):
            for col_off in range(-n + 1, n):
                largest_overlap = max(largest_overlap, overlap_ones(img1, img2, row_off, col_off))
        return largest_overlap
            

# OR
# https://youtu.be/91S7zABWecc [Time Limit Exceeded]

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        largest_overlap = 0
              
        # shift img1, make sure that the position is inbounds of the other matrix, 
        # then check to see if values are same
        # x_shift, y_shift - shifter values for how we shift the first image
        def helper(x_shift, y_shift):
            num = 0
            # count the ones in each overlapping zone
            for r in range(n):
                for c in range(n):
                    if 0<=c+x_shift<n and 0<=r+y_shift<n and img1[r+y_shift][c+x_shift]==1 and img2[r][c]==1:
                        num += 1
            return num
        
        # loop over all possible combinations of shifting coordinates (x_shift, y_shift)
        # # More specifically, the ranges of x_shift and y_shift are both [-n, n].
        # for x in range(-n, n):
        #     for y in range(-n, n):
        #         largest_overlap = max(largest_overlap, helper(x, y))
        # return largest_overlap
        
        return ([helper(x, y) for y in range(-n, n)  for x in range(-n, n)])


img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]
obj = Solution()
print(obj.largestOverlap(img1, img2))


# Complexity Analysis:
# Let N be the width of the matrix.
# First of all, let us calculate the number of all possible shiftings, (i.e. the number of overlapping zones).
# For a matrix of length N, we have 2(N−1) possible offsets along each axis to shift the matrix. Therefore, there 
# are in total 2(N−1) ⋅ 2(N−1) = 4(N−1)^2 possible overlapping zones to calculate.
# Time Complexity: O(N^4).
# As discussed before, we have in total 4(N-1)^2 possible overlapping zones.
# The size of the overlapping zone is bounded by O(N^2).
# Since we iterate through each overlapping zone to find out the overlapping ones, the overall time complexity of 
# the algorithm would be 4(N-1)^2 . O(N^2) = O(N^4).
# Space Complexity: O(1)