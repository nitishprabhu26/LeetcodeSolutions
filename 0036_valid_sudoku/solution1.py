# We can use the numbers 0 through 8 to represent the boxes, where (r/3) * 3 + (c/3) is used calculate a number 
# in the range from 0 to 8. I.e. the square located at (r, c) belongs to the box (r/3) * 3 + (c/3).

# Approach 1: Hash Set
# OR
# Neetocode: https://youtu.be/TjFXEUCMqI8

# Intuition:
# In a valid sudoku puzzle, each row, column, and box contains digits in the range from 1 through 9 without 
# repetition. To check if the sudoku is valid, for each number, we must check if that number is repeated anywhere 
# in the same row, column, or box. However, it would be very inefficient to read the entire row, column, and box 
# every time we check if a number is a duplicate. Instead, as we are iterating over the numbers in the sudoku, we 
# can use hash sets to store the previously seen numbers in each row, column, and box. 
# Via hash sets, we can determine if the current number already exists in the corresponding row, column, or box in 
# constant time. 

# Algorithm:
# 1.Initialize a list containing 9 hash sets, where the hash set at index r will be used to store previously seen 
#   numbers in row r of the sudoku. Likewise, initialize lists of 9 hash sets to track the columns and boxes too.
# 2.Iterate over each position (r, c) in the sudoku. At each iteration, if there is a number at the current 
#   position:
#   -   Check if the number exists in the hash set for the current row, column, or box. If it does, return false, 
#       because this is the second occurrence of the number in the current row, column, or box.
#   -   Otherwise, update the set responsible for tracking previously seen numbers in the current row, column, and 
#       box. The index of the current box is (r / 3) * 3 + (c / 3) where / represents floor division.
# 3.If no duplicates were found after every position on the sudoku board has been visited, then the sudoku is 
#   valid, so return true.


import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


# OR
# Neetocode:


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue
                    
                if (board[r][c] in rows[r]
                   or board[r][c] in cols[c]
                   or board[r][c] in squares[(r//3, c//3)]):
                    return False
                    
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
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
# Space complexity: O(N^2) because in the worst-case scenario, if the board is full, we need a hash set each with 
# size N to store all seen numbers for each of the N rows, N columns, and N boxes, respectively.