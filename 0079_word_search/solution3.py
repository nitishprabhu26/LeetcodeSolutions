# As once notices, we simply return True if the result of recursive call to backtrack() is positive. Though
# this minor modification would have no impact on the time or space complexity, it would however leave with
# some "side-effect", i.e. the matched letters in the original board would be altered to #.

class Solution(object):
    def exist(self, board, word):
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

        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
obj = Solution()
print(obj.exist(board, word))

# Complexity Analysis
# Time Complexity: O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be
# matched.
# For the backtracking function, initially we could have at most 4 directions to explore, but further the
# choices are reduced into 3 (since we won't go back to where we come from). As a result, the execution trace
# after the first step could be visualized as a 3-ary tree, each of the branches represent a potential
# exploration in the corresponding direction. Therefore, in the worst case, the total number of invocation
# would be the number of nodes in a full 3-nary tree, which is about 3^L.
# We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking
# function in the worst case.
# As a result, overall the time complexity of the algorithm would be O(N⋅3^L).
# Space Complexity: O(L) where L is the length of the word to be matched.
