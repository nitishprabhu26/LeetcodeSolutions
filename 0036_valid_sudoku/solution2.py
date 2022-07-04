# Approach 2: Array of Fixed Length

# Intuition:
# Apart from using a hash set, we can also use an array of fixed length to check for duplicates. Each position(pos)
# in the array represents the status of the number pos + 1. Therefore, we can determine if we have already seen 
# some number in constant time. We need an array for each row, column, and box.

# Algorithm:
# 1.Initialize an array of size N filled with zeros for each row, column, and box, where N is the sudoku board 
#   length, which is 9 in this case.
# 2.Iterate over each position (r, c) in the sudoku. At each iteration, if there is a number at the current 
#   position:
#   -   Check if the number n has been previously seen by checking the n−1 th index in the array. If the value at 
#       this index equals to 1, it means that we have already seen this number, so the sudoku is not valid. We 
#       return false in this case.
#   -   Otherwise, if the value at this position equals 0, then it is the first time encountering this number, so 
#       we update the value at this position to 1 to mark that we have seen this number.
# 3.Once every position on the sudoku board is checked, with no duplicates found, we will return true.


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use an array to record the status
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                # Check the column
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

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
# Space complexity: O(N^2) because we need to create 3N arrays each with size N to store all previously seen 
# numbers for all rows, columns, and boxes.