# Approach: count number of spaces in a sentence
# split() will produce arrays of words from sentence - that's not ok for space complexity.


from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            spaces = 0
            for c in sentence:
                if c == ' ':
                    spaces += 1
            res = max(res, spaces)
        
        return res + 1


# OR
# using count() method

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            c = sentence.count(' ')
            res = max(res, c)
        
        return res + 1

# OR

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(" ") for s in sentences) + 1


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
obj = Solution()
print(obj.mostWordsFound(sentences))


# Complexity Analysis:
# Time complexity : O(M * N), where M is the number of sentences and N is the max number of words 
# in one of the sentences.
# Space complexity : O(1).