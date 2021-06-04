# BFS using deque
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return []

        digitsToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        q = deque(digitsToChar[digits[0]])

        for i in range(1, len(digits)):
            s = len(q)
            while s:
                out = q.popleft()
                for j in digitsToChar[digits[i]]:
                    q.append(out+j)
                s -= 1
        return q


inp_str = "234"
obj = Solution()
print(obj.letterCombinations(inp_str))
