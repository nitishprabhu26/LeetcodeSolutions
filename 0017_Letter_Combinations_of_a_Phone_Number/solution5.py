from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitsToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        stack = []
        answer = []
        num_length = len(digits)

        stack.append("")

        while len(stack) > 0:
            current = stack.pop()
            if len(current) == num_length:
                answer.append(current)
            else:
                current_num_index = len(current)
                for letter in digitsToChar[digits[current_num_index]]:
                    stack.append(current+letter)
        return answer


inp_str = "234"
obj = Solution()
print(obj.letterCombinations(inp_str))
