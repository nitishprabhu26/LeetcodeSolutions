# This problem can be solved as if it is a problem of converting base-26 number system to base-10 number system.

# Approach 1: Right to Left
# https://leetcode.com/problems/excel-sheet-column-number/solution/

# Let's say we want to get the value of title 'AZZC'. 
# This can be broken down as 'A***' + 'Z**' + 'Z*' + 'C'. 
# Here, the *s represent smaller blocks. * means a block of 1-character titles. ** means a block of 2-character 
# titles. There are 26^1 titles in a block of 1-character titles. There are 26^2 titles in a block of 2-character 
# titles.

# Scanning AZZC from right to left while accumulating results:

# First, ask the question, what the value of 'C' is:
# 'C' = 3 x 26^0 = 3 x 1 = 3
# result = 0 + 3 = 3

# Then, ask the question, what the value of 'Z*' is:
# 'Z*' = 26 x 26^1 = 26 x 26 = 676
# result = 3 + 676 = 679

# Then, ask the question, what the value of 'Z**' is:
# 'Z**' = 26 x 26^2 = 26 x 676 = 17576
# result = 679 + 17576 = 18255

# Finally, ask the question, what the value of 'A***' is:
# 'A***' = 1 x 26^3 = 1 x 17576 = 17576
# result = 18255 + 17576 = 35831

# Algorithm:
# - To get indices of alphabets, create a mapping of alphabets and their corresponding values. (1-indexed)
# - Initialize an accumulator variable result.
# - Starting from right to left, calculate the value of the character associated with its position and add it 
# to result.


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        # Decimal 65 in ASCII corresponds to char 'A'
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}
        
        # print(alpha_map)
        n = len(columnTitle)
        for i in range(n):
            cur_char = columnTitle[n - 1 - i]
            result += (alpha_map[cur_char] * (26 ** i))
        return result


columnTitle = "AB"
columnTitle = "ZY"
obj = Solution()
print(obj.titleToNumber(columnTitle))


# Complexity Analysis:
# Time Complexity : O(N) where N is the number of characters in the input string.
# Space Complexity : O(1). Even though we have an alphabet to index mapping, it is always constant.