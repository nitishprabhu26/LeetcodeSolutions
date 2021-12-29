# Neetcode (Recursive Backtracking)
# https://youtu.be/pfiQ_PS1g8E


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # store the value of cells which were already in the path, so that we dont revisit them
        path = set()

        # i is the current charecter within the target word that we are looking for
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                    (r, c) in path):
                return False

            # we found the charecter that we are looking for
            path.add((r, c))

            # look for next charecter in all 4 directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))

            return res

        # bruteforce: run dfs starting from all positions on the board
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False

# (above is case sensitive solution, can be made case insensitive)

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

