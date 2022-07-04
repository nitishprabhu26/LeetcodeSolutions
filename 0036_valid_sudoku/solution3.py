# Approach 3: Bitmasking

# Intuition:
# In Approach 2 we showed how we can use values at different positions of an array to mark whether the number 
# corresponding to each position has been seen or not. Each position in the array can take a value of 0 or 1, 
# which can be represented by a single bit. Therefore, we can improve on the space complexity by using bitmasking.
# For a binary number, each bit can take a value of 0 or 1. We can use a binary number with 9 digits to represent 
# whether numbers 1 through 9 have been visited or not.

# Let's first review the two most commonly used operations for get and set in bitmasking. Such operations on bits 
# are commonly referred to as bitwise operations.
# 1.Check if the i^th bit of a binary number is set to 1: x & (1 << i). If this expression evaluates to 0, the bit 
# is not set.
# 2.Set the i^th bit of a binary number x to 1: x = x | (1 << i)

# Algorithm:
# 1.Use an integer for each row, column, and box to track which numbers have been previously seen. The i^th bit 
#   from the right marks the previous occurrence of the number i. For example, '000001010' signifies the numbers 
#   2 and 4 have been previously seen.
# 2.Iterate over each position (r, c) in the sudoku. At each iteration, if there is a number at the current 
#   position:
#   -   Use x & (1 << i) to check if we have seen the number i + 1 previously. If x & (1 << i) is nonzero, then 
#       the number i + 1 is a duplicate and the sudoku is not valid.
#   -   Otherwise, we haven't seen this number before, and we will use x | (1 << i) to set the i^th bit from the 
#       right to signify the number i + 1 has been seen.
# 3.Once every position on the sudoku board is checked, with no duplicates found, we will return true.


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                # Check the column
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)

        return True


board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
print(obj.isValidSudoku(board))


# Complexity Analysis:
# Let N be the board length, which is 9 in this question. Note that since the value of N is fixed, the time and 
# space complexity of this algorithm can be interpreted as O(1). However, to better compare each of the presented 
# approaches, we will treat N as an arbitrary value in the complexity analysis below.
# Time complexity: O(N^2) because we need to traverse every position in the board, and each of the four check steps
# is an O(1) operation.
# Space complexity: O(N) because in the worst-case scenario, if the board is full, we need 3N binary numbers to 
# store all seen numbers in all rows, columns, and boxes. Using a binary number to record the occurrence of 
# numbers is probably the most space-efficient method.