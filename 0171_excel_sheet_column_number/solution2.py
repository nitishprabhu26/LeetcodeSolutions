# Approach 2: Left to Right
# https://leetcode.com/problems/excel-sheet-column-number/solution/
# OR
# https://youtu.be/g-l4UpF62x0


# Intuition:
# Rather than scanning from right to left as described in Approach 1, we can also scan the title from left to 
# right.

# For example, if we want to get the decimal value of string "1337", we can iteratively find the result by 
# scanning the string from left to right as follows:
# '1' = 1
# '13' = (1 x 10) + 3 = 13
# '133' = (13 x 10) + 3 = 133
# '1337' = (133 x 10) + 7 = 1337

# Instead of base-10, we are dealing with base-26 number system. Based on the same idea, we can just replace 10s 
# with 26s and convert alphabets to numbers.
# For a title "LEET":
# L = 12
# E = (12 x 26) + 5 = 317
# E = (317 x 26) + 5 = 8247
# T = (8247 x 26) + 20 = 214442

# In Approach 1, we have built a mapping of alphabets to numbers. There is another way to get the number value of 
# a character without building an alphabet mapping, which is shown here.


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = (result * 26) + (ord(columnTitle[i]) - ord('A') + 1)
        return result

# OR

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            d = ord(c) - ord('A') + 1
            result = (result * 26) + d
        return result


columnTitle = "AB"
columnTitle = "ZY"
obj = Solution()
print(obj.titleToNumber(columnTitle))


# Complexity Analysis:
# Time Complexity : O(N) where N is the number of characters in the input string.
# Space Complexity : O(1).