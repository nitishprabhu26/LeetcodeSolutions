# Approach : Using Two arrays
# Also, used two dictionaries in approach 1


from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        def matches(word, pattern):
            # patterns and all words contain only lowercase letters
            patternToWord = [None] * 26
            wordToPattern = [None] * 26
            
            # given, words[i].length == pattern.length
            for index in range(len(word)):
                patternChar = pattern[index]
                wordChar = word[index]
                
                if patternToWord[ord(patternChar) - ord('a')] is None:
                    patternToWord[ord(patternChar) - ord('a')] = wordChar
                
                if wordToPattern[ord(wordChar) - ord('a')] is None:
                    wordToPattern[ord(wordChar) - ord('a')] = patternChar
                
                if (patternToWord[ord(patternChar) - ord('a')] != wordChar) or (wordToPattern[ord(wordChar) - ord('a')] != patternChar):
                        return False
                
            return True
                        
        for word in words:
            if matches(word, pattern):
                result.append(word)     
        
        return result


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
obj = Solution()
print(obj.findAndReplacePattern(words, pattern))


# Complexity Analysis
# Time Complexity: O(N * K), where N is the number of words, and K is the length of each word.
# Space Complexity: O(N * K), the space used by the answer.