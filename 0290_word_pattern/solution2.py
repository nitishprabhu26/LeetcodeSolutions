# Neetcode: using 2 HashMaps
# https://youtu.be/W_akoecmCbM


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            
            # mapping it first time or remapping it again based on the if condition
            charToWord[c] = w
            wordToChar[w] = c
            
        return True

pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))


# Complexity Analysis
# Time Complexity: O(N) where N represents the number of words in s or the number of characters in pattern.
# Space Complexity: O(M) where M represents the number of unique words in s. Even though we have two hash 
# maps, the character to word hash map has space complexity of O(1) since there can at most be 26 keys.

