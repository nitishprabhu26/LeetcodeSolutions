# Approach: store row indexed words and column index words; compare them for equality

from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        row_word_list = words
        no_of_cols = 0
        
        # for the cases: ["abc","bde","cefg"] or ["c", "bd"] etc
        for word in words:
            no_of_cols = max(no_of_cols, len(word))
        col_word_list = [''] * max(len(words), no_of_cols)
        
        # create column index words
        for row in range(len(words)):
            for col in range(len(words[row])):
                col_word_list[col] += words[row][col]
        
        # check for equality
        for i in range(len(row_word_list)):
            if row_word_list[i] != col_word_list[i]:
                return False
            
        return True


words = ["abcd","bnrt","crmy","dtye"]
# words = ["abc","bde","cefg"]
obj = Solution()
print(obj.validWordSquare(words))


# Complexity Analysis:
# Here, n is the number of strings in the words array and m is the maximum length of a string.
# Time complexity : O(n.m).
# Space complexity : O(n.m).