# Approach 2: Iterate on the Matrix

# Intuition:
# The previous approach is fairly efficient in terms of run-time and will be accepted, but we can still optimize 
# it further.
# We were generating and storing the words represented by each column and then we were comparing them with words 
# represented by rows. Instead, we can directly iterate over the k^th row and column characters simultaneously and 
# check if all positions have the same characters or not without storing them.
# This will help in saving computation time like generating new words and comparing them at the end, and the space 
# used to store them.
# We will keep a variable wordNum to represent the index of the row and column and a variable currPos to point to 
# the current index of the word of the current row and column. Then we will increment currPos to match all 
# characters of the current row and column. If all characters match we move to the next word, thus incrementing 
# wordNum and checking again.

# Algorithm:
# 1. Initialize variables:
#    -  wordNum, representing the number of the row and column of the current word.
#    -  charPos, representing the index of the current character of the wordNum word.
# 2. Iterate over each wordNum from 0 to words.size() - 1, representing the number of each word:
#    -  Then we iterate over each character charPos from 0 to words[wordNum].size() - 1:
#       -   If currPos is greater than or equal to words.size(), that is, the word represented by the wordNum-th 
#           row is larger than the respective column's word, or
#       -   if wordNum is greater than or equal to words[charPos].size(), that is, the word represented by the 
#           wordNum-th column is larger than the respective row's word, or
#       -   if the character at index (wordNum, charPos) does not match character at index (charPos, wordNum) in 
#           matrix, then we return false.
# 3. At the end all words represented by each row would have matched with words represented by respective columns, 
#    thus we will return true.


from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                # char_pos (curr 'row' word) is bigger than column word, or
                # word_num (curr 'column' word) is bigger than row word, or 
                # characters at index (word_num,char_pos) and (char_pos,word_num) are not equal.
                if char_pos >= len(words) or \
                    word_num >= len(words[char_pos]) or \
                    words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True


words = ["abcd","bnrt","crmy","dtye"]
# words = ["abc","bde","cefg"]
obj = Solution()
print(obj.validWordSquare(words))


# Complexity Analysis:
# Here, n is the number of strings in the words array and m is the maximum length of a string.
# Time complexity : O(n.m).
# - We iterate over all characters of a word represented by a row and column which will take O(m) time, thus for n 
#   rows we will take O(n⋅m) time.
# Space complexity : O(n.m).
# - We are not using any auxiliary space.