# Approach 1: Greedy
# https://leetcode.com/problems/integer-to-roman/solution/

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []

        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0:
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits
            roman_digits.append(symbol*count)
        return "".join(roman_digits)


num = 6
obj = Solution()
print(obj.intToRoman(num))


# Complexity Analysis:

# Time complexity : O(1).
# As there is a finite set of roman numerals, there is a hard upper limit on how many times the loop can iterate.
# This upper limit is 15 times, and it occurs for the number 3888, which has a representation of MMMDCCCLXXXVIII.
# Therefore, we say the time complexity is constant, i.e. O(1)O(1).

# Space complexity : O(1).
# The amount of memory used does not change with the size of the input integer, and is therefore constant.
