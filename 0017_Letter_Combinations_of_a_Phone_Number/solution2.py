# Approach 1: Backtracking
# Backtracking is a general algorithm for finding all solutions to some computational problems, notably 
# constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a 
# candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitsToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            for c in digitsToChar[digits[index]]:
                # Add the letter to our current path
                path.append(c)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        res = []
        backtrack(0, [])
        return res


inp_str = "234"
obj = Solution()
print(obj.letterCombinations(inp_str))


# Complexity Analysis:

# Time complexity: O((4^N). N), where N is the length of digits. Note that 4 in this expression is referring 
# to the maximum value length in the hash map, and not to the length of the input.
# The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional 
# paths for every extra digit.

# Space complexity: O(N), where N is the length of digits.
# Not counting space used for the output. The extra space we use relative to input size is the space occupied 
# by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we 
# reach that depth, we backtrack.
# As the hash map does not grow as the inputs grows, it occupies O(1) space.
