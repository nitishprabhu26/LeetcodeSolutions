# Approach 1: Storing New Words
# https://leetcode.com/problems/valid-word-square/solution/

# Intuition:
# We can start this problem by thinking of generating and storing the new words, (i.e. words represented by each 
# column) and then matching them with the respective row's words.
# We will take an empty strings array newWords and fill it by generating new words by iterating on the matrix 
# column-wise.
# In the end, we will check if both the array's words at the same index match or not.

# Also we can make note of two facts: (https://leetcode.com/problems/valid-word-square/solution/)
# - First, to form a valid square the number of rows and columns must be equal.
# - Second, in a valid square, the first row must have the most characters


# Algorithm:
# 1. Initialize variables:
#    -  cols to 0, used to store the maximum number of charaters of any word in the matrix.
#    -  rows to words.size(), used to store the number of rows in the matrix.
#    -  newWords, an empty string array to store new words represented by each column of the matrix.
# 2. Iterate over all elements in the words array and store the length of the maximum length word in cols which 
#    will be the number of columns in the matrix.
# 3. If the first row doesn't have the maximum number of characters or the number of rows is not equal to the 
#    number of columns, we can't form a valid square thus we can return false.
# 4. For each column col from 0 to cols - 1:
#    -  We initialize an empty string variable newWord.
#    -  Then, we iterate over each row row, and if a character exists at the current position (row, col) in the 
#       matrix we append it in newWord.
#    -  After generating the word newWord represented by the current column col, we store it in newWords array.
# 5. At the end, if newWords and words have the same elements at the same index we return true, otherwise return 
#    false.


from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = 0
        rows = len(words)
        new_words = []
        
        for word in words:
            cols = max(cols, len(word))

        # If the first row doesn't have maximum number of charaters, or
        # the number of rows is not equal to columns it can't form a square.
        if cols != len(words[0]) or rows != cols:
            return False

        for col in range(cols):
            new_word = []
            # Iterate on each character of column 'col'.
            for row in range(rows):
                # If the current row's word's size is less than the column number it means this column is empty,
                # or, if there is a character present then use it to make the new word.
                if col < len(words[row]):
                    new_word.append(words[row][col])
            # Push the new word of column 'col' in the list.
            new_words.append(''.join(new_word))

        # Check if all row's words match with the respective column's words.
        return words == new_words


words = ["abcd","bnrt","crmy","dtye"]
# words = ["abc","bde","cefg"]
obj = Solution()
print(obj.validWordSquare(words))


# Complexity Analysis:
# Here, n is the number of strings in the words array and m is the maximum length of a string.
# Time complexity : O(n.m).
# - We iterate on the words array to find the maximum number of characters in a word in O(n) time.
# - Then we iterate over each element of a column to form a word which will take O(n) time, so for m columns, 
#   it will take O(n⋅m) time.
# - At the end, we compare strings at same index in words and newWords arrays which will take O(m) time for each 
#   index, so for n strings, we will take O(n⋅m) time.
# - Thus, overall we take O(n⋅m) time.
# Space complexity : O(n.m).
# - We are storing n strings of length m in an additional array. Thus, we use O(n⋅m) space.