# Approach 1: Backtracking (similar to neetcode)
# A more accurate term to summarize the solution would be backtracking instead of DFS, which is a methodology 
# where we mark the current path of exploration, if the path does not lead to a solution, we then revert the 
# change (i.e. backtracking) and try another path.
# In addition, the exploration is done via the DFS strategy, where we go as further as possible before we try 
# the next direction.


# Algorithm:
# The skeleton of the algorithm is a loop that iterates through each cell in the grid. For each cell, we invoke 
# the backtracking function (i.e. backtrack()) to check if we would obtain a solution, starting from this very 
# cell.
# For the backtracking function backtrack(row, col, suffix), as a DFS algorithm, it is often implemented as a 
# recursive function. The function can be broke down into the following four steps:
# Step 1). At the beginning, first we check if we reach the bottom case of the recursion, where the word to be 
# matched is empty, i.e. we have already found the match for each prefix of the word.
# Step 2). We then check if the current state is invalid, either the position of the cell is out of the 
# boundary of the board or the letter in the current cell does not match with the first letter of the word.
# Step 3). If the current step is valid, we then start the exploration of backtracking with the strategy of 
# DFS. First, we mark the current cell as visited, e.g. any non-alphabetic letter will do. Then we iterate 
# through the four possible directions, namely up, right, down and left. The order of the directions can be 
# altered, to one's preference.
# Step 4). At the end of the exploration, we revert the cell back to its original state. Finally we return the 
# result of the exploration.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False
    
    
    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
obj = Solution()
print(obj.exist(board, word))


# Complexity Analysis:
# Time complexity : O(n * m * dfs). since we call dfs for every position on the board.
#                   O(n * m * 4^L) (goes in all 4 directions)
#                   where n, m are dimensions of the board, and L is the length of the board.
# Space complexity : O(L) where L is the length of the word to be matched.
# The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length 
# of the call stack would be the length of the word.

