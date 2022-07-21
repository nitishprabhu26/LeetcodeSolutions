# Approach: Using python's find() method
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/2310521/Simple-oror-Python-oror-Brute-Force-oror-84-Speed-oror-97-Memory


# using while loop:

from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(s, word) -> bool:
            pos = -1
            i = 0
            while i < len(word):
                pos = s.find(word[i], pos + 1)
                if pos == -1:
                    return False
                i += 1
                
            return True

        count = 0
        for word in words:
            if isSubsequence(s, word):
                count += 1
                
        return count


# using for loop:

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(s, word) -> bool:
            pos = -1
            for c in word:
                pos = s.find(c, pos + 1)
                if pos == -1:
                    return False
                
            return True

        count = 0
        for word in words:
            if isSubsequence(s, word):
                count += 1
                
        return count


# without using helper function:

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            pos = -1
            for c in word:
                pos = s.find(c, pos + 1)
                if pos == -1:
                    break
                    
            if pos != -1:
                count += 1
                
        return count


s = "abcde"
words = ["a","bb","acd","ace"]
obj = Solution()
print(obj.numMatchingSubseq(s, words))